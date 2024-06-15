from datetime import datetime, timedelta
from typing import List, overload

from src.models import TickerPrice


class PriceNowRepository:
    def __init__(self, db) -> None:
        self._db = db

    @overload
    def save(self, ticker_prices: TickerPrice) -> None:
        ...

    @overload
    def save(self, ticker_prices: List[TickerPrice]) -> None:
        ...

    def save(self, ticker_prices: TickerPrice | List[TickerPrice]) -> None:
        if isinstance(ticker_prices, list):
            self._db.save([ticker.as_dict() for ticker in ticker_prices])
        else:
            self._db.save(ticker_prices.as_dict())

    def find_all(self) -> List[TickerPrice]:
        ticker_prices = self._db.find_all()
        return [TickerPrice(**ticker) for ticker in ticker_prices]

    def find_by_last_time(self, time: timedelta) -> List[TickerPrice]:
        last_time = datetime.now() - time
        ticker_prices = self.find_all()
        last_time_ticker_prices = [ticker for ticker in ticker_prices if ticker.timestamp > last_time]
        return last_time_ticker_prices
