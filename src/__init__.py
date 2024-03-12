import json

from dotenv import load_dotenv

from api import Binance

load_dotenv()

binance = Binance()

with open('my_coins.json', 'w') as file:
    response = binance.my_coins()
    file.write(json.dumps([r.as_dict() for r in response]))

with open('trade_24h.json', 'w') as file:
    response = binance.statistics_24hr_by_usdt()
    # file.write(json.dumps([r.as_dict() for r in response]))
    file.write(json.dumps([r.as_dict() for r in binance.price_now_by_usdt()]))
    # for r in response:
    #     print(f'{r.symbol}: {r.priceChangePercent}')
