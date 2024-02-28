import requests
from dotenv import load_dotenv
import os



load_dotenv()
api_key = os.getenv('API_KEY')

currency = requests.get("https://api.currencyapi.com/v3/latest",params={"apikey": api_key})

exchanges = currency.json()

def main():
    print('welcome to global currency conversion')
