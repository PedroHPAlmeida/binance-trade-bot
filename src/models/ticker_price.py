from datetime import datetime
from typing import Any, Dict


class TickerPrice:
    def __init__(self, **kwargs):
        self.symbol: str = kwargs['symbol']
        self.price = float(kwargs['price'])
        self.timestamp = datetime.fromisoformat(kwargs.get('timestamp', datetime.now().isoformat()))

    def as_dict(self) -> Dict[str, Any]:
        return {'symbol': self.symbol, 'price': self.price, 'timestamp': self.timestamp.isoformat()}

    def __str__(self) -> str:
        return str(self.as_dict())
