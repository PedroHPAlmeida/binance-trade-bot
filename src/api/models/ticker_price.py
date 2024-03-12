from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class TickerPrice:
    symbol: str
    price: float

    def __post_init__(self):
        self.price = float(self.price)

    def as_dict(self) -> Dict[str, Any]:
        return {"symbol": self.symbol, "price": self.price}
