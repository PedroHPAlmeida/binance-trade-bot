import os

import requests


class Telegram:
    def __init__(self, token: str = os.getenv('TELEGRAM_BOT_TOKEN')):
        self._token = token
        self._api_url = f'https://api.telegram.org/bot{token}'
        self._chat_id = os.getenv('TELEGRAM_CHAT_ID')

    def send_message(self, message: str):
        data = {'chat_id': self._chat_id, 'text': message}
        url = f'{self._api_url}/sendMessage'
        requests.post(url, data)
