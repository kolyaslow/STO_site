from flask import Flask, render_template, request, flash
from telegram.send_telegram_message import send_telegram_message
from string import ascii_letters, punctuation, whitespace
from keys_and_id import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

def data_validity_check(form):
    #проверка имени на содержание не русских символов
    for char in form['name']:
        if  char in ascii_letters + punctuation + whitespace:
            return 'Имя должно содержать только русские символы'

    if len(form['vin_number']) > 17:
        return 'Vin номер должен содержать не более 17 символов'

    # проверка на содержание спец сиволов
    for char in form['vin_number']:
        if char in punctuation:
            return 'Не корректный Vin номер'

    #проверка номера талефона
    if len(form['phone_number']) > 17:
        return 'Номер телефона должен содержать не более 11 символов'

    if not form['phone_number'].isdigit():
        return 'Недопустимые символы в номере телефона'

    return 'Форма отправлена, ждите звонка'


@app.route('/', methods=['POST', 'GET'])
def main_page():

    if request.method == 'POST':
        form = request.form
        error_data_or_ok = data_validity_check(form)
        if error_data_or_ok == 'Успешная отправка':

            message = f"Имя: {form['name']} \n" \
                        f"Номер телефона: {form['phone_number']} \n" \
                        f"VIN номер: {form['vin_number']} \n" \
                        f"Услуга: {form['service']}"
            send_telegram_message(message)
            flash(error_data_or_ok, category='sent_successfully')
        else:
            #ормирование подсказок отправки формы
            flash(error_data_or_ok, category='error')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)