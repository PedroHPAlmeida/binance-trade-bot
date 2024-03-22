from .app.api import Binance
from .app.db import Mongo
from .app.repository import PriceNowRepository, Statistics24hRepository

binance = Binance()


def handler(event, context):
    save_trades_24h()
    save_prices_now()


def save_trades_24h():
    statistics_24h_repo = Statistics24hRepository(Mongo('trades', 'statistics_24hr_by_usdt'))
    trades_24h = binance.statistics_24hr_by_usdt()
    statistics_24h_repo.save(trades_24h)


def save_prices_now():
    price_now_repo = PriceNowRepository(Mongo('trades', 'price_now_by_usdt'))
    prices_now = binance.price_now_by_usdt()
    price_now_repo.save(prices_now)
