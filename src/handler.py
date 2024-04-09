from binance import Binance
from mongo import Mongo
from price_now_repo import PriceNowRepository
from statistics_24hr_repo import Statistics24hRepository

binance = Binance()


def handler(event, context):
    try:
        # save_trades_24h()
        # save_prices_now()
        return {'status': 'success'}
    except Exception as ex:
        return {'status': 'error', 'message': str(ex)}


def save_trades_24h():
    statistics_24h_repo = Statistics24hRepository(Mongo('trades', 'statistics_24hr_by_usdt'))
    trades_24h = binance.statistics_24hr_by_usdt()
    statistics_24h_repo.save(trades_24h)


def save_prices_now():
    price_now_repo = PriceNowRepository(Mongo('trades', 'price_now_by_usdt'))
    prices_now = binance.price_now_by_usdt()
    price_now_repo.save(prices_now)
