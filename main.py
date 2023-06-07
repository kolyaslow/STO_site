from flask import Flask, render_template, request, flash
from telegram.send_telegram_message import send_telegram_message
from string import ascii_letters, punctuation, whitespace
from keys_and_id import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

name_error = 'Имя должно содержать только русские символы'
len_vin_number_error = 'Vin номер должен содержать не более 17 символов'
vin_number_error = 'Не корректный Vin номер'
len_phone_number_error = 'Номер телефона должен содержать не более 11 символов'
phone_number_error = 'Недопустимые символы в номере телефона'
sent_successfully = 'Форма отправлена, ждите звонка'
def data_validity_check(form):
    #проверка имени на содержание не русских символов
    for char in form['name']:
        if  char in ascii_letters + punctuation + whitespace:
            return name_error

    if len(form['vin_number']) > 17:
        return len_vin_number_error

    # проверка на содержание спец сиволов
    for char in form['vin_number']:
        if char in punctuation:
            return vin_number_error

    #проверка номера талефона
    if len(form['phone_number']) > 11:
        return len_phone_number_error

    if not form['phone_number'].isdigit():
        return phone_number_error

    return sent_successfully


@app.route('/', methods=['POST', 'GET'])
def main_page():

    if request.method == 'POST':
        form = request.form
        error_data_or_ok = data_validity_check(form)
        if error_data_or_ok == sent_successfully:

            message = f"Имя: {form['name']} \n" \
                        f"Номер телефона: {form['phone_number']} \n" \
                        f"VIN номер: {form['vin_number']} \n" \
                        f"Услуга: {form['service']}"

            if send_telegram_message(message):
                #подсказка формы - успешная отправка
                flash(error_data_or_ok, category='sent_successfully')
            else:
                flash('Ошибка отправки сообщения', category='error')
        else:
            #ормирование ошибок для формы
            flash('*' + error_data_or_ok, category='error')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)