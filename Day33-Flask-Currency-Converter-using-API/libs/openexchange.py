import requests

class OpenExchangeClient:
    BASE_POINT = "https://openexchangerates.org/api/latest.json"
    def __init__(self, app_id):
        self.app_id = app_id

    @property
    def exchange_rates(self):
        response = requests.get(f"{self.BASE_POINT}?app_id={self.app_id}")
        rates = response.json()['rates']
        return rates




