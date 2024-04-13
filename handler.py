from datetime import datetime

from src.apis import Binance, GeminiAI, Telegram
from src.db import Mongo, PriceNowRepository, Statistics24hRepository

binance = Binance()
PROMPTS = {
    'success': "I developed a script that runs every 'X' minutes and when it finishes running, a notification is sent by a Telegram Bot. \
I want you to write a creative message stating that the script ran successfully. \
As the message will be sent via Telegram, avoid characters that will not be interpreted correctly. \
Use emojis as much as you like. The structure of the message must consist of a title, body and conclusion. \
However, don't put the words 'Title', 'Message:' and 'Conclusion:' explicitly, just follow the structure. \
Keep an average of approximately 400 characters in your response. \
I will also give you the script execution timestamp, include it somewhere in the message. \
The timestamp is UTC 0, convert it to UTC +3 and format the date and time in the following pattern: dd/MM/YYYY hh:mm:ss. \
Below is the execution time of the script ${execution_time}. The message must be written entirely in Brazilian Portuguese.",
    'error': "I developed a script that runs every 'X' minutes and when it finishes running, a notification is sent by a Telegram Bot. \
I want you to write a creative message stating that an error occurred while running the script. \
As the message will be sent via Telegram, avoid characters that will not be interpreted correctly. Use emojis as much as you want. \
The structure of the message must consist of title, body and conclusion. \
However, don't put the words 'Title', 'Message:' and 'Conclusion:' explicitly, just follow the structure. \
Keep your response to an average of approximately 400 characters. \
I will also give you the script execution timestamp by including it somewhere in the message. \
The timestamp is UTC 0, convert it to UTC +3 and format the date and time in the following pattern: dd/MM/YYYY hh:mm:ss. \
Below is the execution time of the ${execution_time} script. Also include the error that occurred during execution, the error follows: ${error}. \
The message must be written entirely in Brazilian Portuguese.",
}


def handler(event, context):
    try:
        save_trades_24h()
        save_prices_now()
        send_message(define_message('success'))
        return {'status': 'success'}
    except Exception as ex:
        send_message(define_message('error', error=str(ex)))
        return {'status': 'error', 'message': str(ex)}


def save_trades_24h():
    statistics_24h_repo = Statistics24hRepository(Mongo('trades', 'statistics_24hr_by_usdt'))
    trades_24h = binance.statistics_24hr_by_usdt()
    statistics_24h_repo.save(trades_24h)


def save_prices_now():
    price_now_repo = PriceNowRepository(Mongo('trades', 'price_now_by_usdt'))
    prices_now = binance.price_now_by_usdt()
    price_now_repo.save(prices_now)


def define_message(status: str, **kwargs) -> str:
    ai = GeminiAI()
    message = PROMPTS[status]
    kwargs['execution_time'] = datetime.now().isoformat()
    for key, value in kwargs.items():
        message = message.replace(f'${key}', value)
    return ai.generate(message)


def send_message(message: str):
    telegram = Telegram()
    telegram.send_message(message)
