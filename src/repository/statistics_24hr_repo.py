from typing import overload, List
from models import Trade24hData


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
