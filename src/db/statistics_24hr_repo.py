from datetime import datetime, timedelta
from typing import List, overload

from src.models import Trade24hData


class Statistics24hRepository:
    def __init__(self, db) -> None:
        self._db = db

    @overload
    def save(self, trades: Trade24hData) -> None:
        ...

    @overload
    def save(self, trades: List[Trade24hData]) -> None:
        ...

    def save(self, trades: Trade24hData | List[Trade24hData]) -> None:
        if isinstance(trades, list):
            self._db.save([trade.as_dict() for trade in trades])
        else:
            self._db.save(trades.as_dict())

    def find_all(self) -> List[Trade24hData]:
        trades = self._db.find_all()
        return [Trade24hData(**trade) for trade in trades]

    def find_by_last_time(self, time: timedelta) -> List[Trade24hData]:
        last_time = datetime.now() - time
        trades = self.find_all()
        last_time_trades = [trade for trade in trades if trade.timestamp > last_time]
        return last_time_trades
