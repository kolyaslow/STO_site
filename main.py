from flask import Flask, render_template, request
from .telegram.send_telegram_message import send_telegram_message

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        form = request.form
        message = f"Имя: {form['name']} \n" \
                    f"Номер телефона: {form['phone_number']} \n" \
                    f"VIN номер: {form['vin_number']} \n" \
                    f"Услуга: {form['service']}"
        print(message)
        send_telegram_message(message)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)