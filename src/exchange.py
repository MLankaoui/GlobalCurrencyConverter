import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def exchange(user_currency, target_currency, amount):
    print(f'nice you chose {user_currency}/{target_currency} , with the amount of {amount}')

    currency = requests.get(f"https://api.currencyapi.com/v3/latest",params={"apikey": api_key, "base_currency": {target_currency}})

    exchanges = currency.json()

    result = float(amount) * (exchanges['data'][user_currency]['value'])
    print(f'Your result is: {result} {user_currency}')
    

