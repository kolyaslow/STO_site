from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_wtf import CSRFProtect

from forms import RequestForm
from telegram.send_telegram_message import send_telegram_message
from string import ascii_letters, punctuation, whitespace
from keys_and_id import SECRET_KEY
from re import match


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

name_error = 'Имя должно содержать только русские символы'
len_vin_number_error = 'Vin номер должен содержать не более 17 символов'
vin_number_error = 'Не корректный Vin номер'
len_phone_number_error = 'Номер телефона должен содержать не более 11 символов'
phone_number_error = 'Недопустимые символы в номере телефона'
sent_successfully = 'Заявка отправлена, ждите звонка'


def data_validity_check(form):
    #проверка имени на содержание не русских символов
    for char in form.name.data:
        if  char in ascii_letters + punctuation + whitespace:
            return name_error

    if len(form.vin_number.data) > 17:
        return len_vin_number_error

    # проверка на содержание спец сиволов
    if not match(r'^[A-HJ-NPR-Z0-9]{17}$', form.vin_number.data):
        return vin_number_error

    #проверка номера талефона
    if len(form.phone_number.data) > 11:
        return len_phone_number_error

    if not form.phone_number.data.isdigit():
        return phone_number_error

    return sent_successfully


@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        form = RequestForm(request.form)
        error_data_or_ok = data_validity_check(form)

        if error_data_or_ok == sent_successfully:

            message = f"Имя: {form.name.data} \n" \
                        f"Номер телефона: {form.phone_number.data} \n" \
                        f"VIN номер: {form.vin_number.data} \n" \
                        f"Услуга: {form.service.data}"

            if send_telegram_message(message):
                #подсказка формы - успешная отправка
                flash(error_data_or_ok, category='sent_successfully')
            else:
                flash('Ошибка отправки сообщения', category='error')

        else:
            #ормирование ошибок для формы
            flash('*' + error_data_or_ok, category='error')
            #перенаправление на форму, для дальнейшего заполнения
        return redirect(url_for('main_page') + '#MESS')

    else:
        form = RequestForm()

    return render_template('index2.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)



