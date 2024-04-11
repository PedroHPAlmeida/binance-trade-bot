import os
from typing import Any, Dict, List

from binance.spot import Spot

from src.models import MyCoin, TickerPrice, Trade24hData


class Binance:
    def __init__(self, client=None) -> None:
        self._client = client if client else Spot(api_key=os.getenv('BINANCE_API_KEY'), api_secret=os.getenv('BINANCE_SECRET_KEY'))
        self._recv_window = 60000

    def ping(self) -> None:
        self._client.ping()

    def my_account(self) -> Dict[str, Any]:
        return self._client.account(recvWindow=self._recv_window)

    def my_coins(self, min_value: int = 0) -> List[MyCoin]:
        account = self.my_account()
        balances = account.get('balances', [])
        greater_zero = list(filter(lambda b: float(b['free']) > min_value or float(b['locked']) > min_value, balances))
        return list(map(lambda b: MyCoin(**b), greater_zero))

    def statistics_24hr_by_usdt(self) -> List[Trade24hData]:
        results = self._client.ticker_24hr()
        usdt_pairs = list(filter(lambda r: r.get('symbol', '').endswith('USDT'), results))
        coins = list(map(lambda r: Trade24hData(**r), self._remove_suffix(usdt_pairs)))
        return sorted(coins, key=lambda c: c.priceChangePercent, reverse=True)

    def price_now_by_usdt(self) -> List[TickerPrice]:
        response = self._client.ticker_price()
        by_usdt = list(filter(lambda r: r['symbol'].endswith('USDT'), response))
        return [TickerPrice(**r) for r in self._remove_suffix(by_usdt)]

    def avg_price_by_usdt(self, coin: str):
        return self._client.avg_price(f'{coin.upper()}USDT')

    def _remove_suffix(self, symbols: List[Dict[str, Any]], suffix: str = 'USDT'):
        return [{**s, 'symbol': s['symbol'].replace(suffix, '')} for s in symbols]
