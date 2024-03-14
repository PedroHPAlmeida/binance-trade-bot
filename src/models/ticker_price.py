from datetime import datetime
from typing import Any, Dict


class TickerPrice:
    def __init__(self, **kwargs):
        self.symbol: str = kwargs['symbol']
        self.price = float(kwargs['price'])
        self.timestamp = datetime.now().isoformat()

    def as_dict(self) -> Dict[str, Any]:
        return self.__dict__

    def __str__(self) -> str:
        return str(self.as_dict())
