from src.apis import LLM, Binance, Telegram, get_prompt
from src.db import Mongo, PriceNowRepository, Statistics24hRepository
from src.utils import utils
from src.recommendations import Recommend

binance = Binance()
price_now_repo = PriceNowRepository(Mongo('trades', 'price_now_by_usdt'))
statistics_24h_repo = Statistics24hRepository(Mongo('trades', 'statistics_24hr_by_usdt'))
recommend = Recommend(price_now_repo, statistics_24h_repo)


def handler(event, context):
    try:
        save_trades_24h()
        save_prices_now()
        # send_message(define_message('success'))
        send_message(recommend.most_valued())
        return {'status': 'success'}
    except Exception as ex:
        send_message(define_message('error', error=str(ex)))
        return {'status': 'error', 'message': str(ex)}


def save_trades_24h():
    trades_24h = binance.statistics_24hr_by_usdt()
    statistics_24h_repo.save(trades_24h)


def save_prices_now():
    prices_now = binance.price_now_by_usdt()
    price_now_repo.save(prices_now)


def define_message(status: str, **kwargs) -> str:
    ai = LLM()
    message = get_prompt(status)
    kwargs['execution_time'] = utils.timestamp_ptbr()
    return ai.generate(message, **kwargs)


def send_message(message: str):
    telegram = Telegram()
    telegram.send_message(message)
