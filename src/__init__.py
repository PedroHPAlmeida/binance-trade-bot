import json

from dotenv import load_dotenv

from api import Binance

load_dotenv()

binance = Binance()

with open('balances.json', 'w') as file:
    balances = binance.get_balances(0)
    file.write(json.dumps(balances))
