import os
from typing import Any, Dict, List

from binance.spot import Spot


class Binance:
    def __init__(self, api_key: str = os.getenv('BINANCE_API_KEY'), secret_key: str = os.getenv('BINANCE_SECRET_KEY')) -> None:
        self._api_key = api_key
        self._secret_key = secret_key
        self._client = Spot(api_key=os.getenv('BINANCE_API_KEY'), api_secret=os.getenv('BINANCE_SECRET_KEY'))
        self._recv_window = 60000

    def get_account(self) -> Dict[str, Any]:
        return self._client.account(recvWindow=self._recv_window)

    def get_balances(self, min_value: int = 0) -> List[Dict[str, Any]]:
        account = self.get_account()
        balances = account.get('balances', [])
        return list(filter(lambda b: float(b['free']) > min_value or float(b['locked']) > min_value, balances))
