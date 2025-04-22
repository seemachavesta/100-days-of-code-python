
from flask import Flask, render_template, url_for, request
from libs.openexchange import  OpenExchangeClient

app = Flask(__name__)

APP_ID = "f646830be9d94b368116f6ee6bc8fa42"
client = OpenExchangeClient(APP_ID)


@app.route('/', methods=['GET'])
def home():
    rates = client.exchange_rates
    return render_template('index.html', rates= rates.keys(), result=None)


@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    target_currency = request.form['currency']

    rates = client.exchange_rates
    rate = rates.get(target_currency)

    if rate:
        converted = round(amount * rate, 2)
        return render_template('index.html', rates=rates.keys(), result=converted, amount=amount, target_currency=target_currency )
    else:
        return render_template('index.html', rates=rates.keys(), result="Invalid currency", amount=amount,
                               target_currency=target_currency)







if __name__ == '__main__':
    app.run(debug=True)



