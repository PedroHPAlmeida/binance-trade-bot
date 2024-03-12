from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Trade24hData:
    symbol: str
    priceChange: float
    priceChangePercent: float
    weightedAvgPrice: float
    prevClosePrice: float
    lastPrice: float
    lastQty: float
    bidPrice: float
    bidQty: float
    askPrice: float
    askQty: float
    openPrice: float
    highPrice: float
    lowPrice: float
    volume: float
    quoteVolume: float
    openTime: int
    closeTime: int
    firstId: int
    lastId: int
    count: int

    def __post_init__(self):
        self.priceChange = float(self.priceChange)
        self.priceChangePercent = float(self.priceChangePercent)
        self.weightedAvgPrice = float(self.weightedAvgPrice)
        self.prevClosePrice = float(self.prevClosePrice)
        self.lastPrice = float(self.lastPrice)
        self.lastQty = float(self.lastQty)
        self.bidPrice = float(self.bidPrice)
        self.bidQty = float(self.bidQty)
        self.askPrice = float(self.askPrice)
        self.askQty = float(self.askQty)
        self.openPrice = float(self.openPrice)
        self.highPrice = float(self.highPrice)
        self.lowPrice = float(self.lowPrice)
        self.volume = float(self.volume)
        self.quoteVolume = float(self.quoteVolume)
        self.openTime = int(self.openTime)
        self.closeTime = int(self.closeTime)
        self.firstId = int(self.firstId)
        self.lastId = int(self.lastId)
        self.count = int(self.count)

    def as_dict(self) -> Dict[str, Any]:
        return {
            'symbol': self.symbol,
            'priceChange': self.priceChange,
            'priceChangePercent': self.priceChangePercent,
            'weightedAvgPrice': self.weightedAvgPrice,
            'prevClosePrice': self.prevClosePrice,
            'lastPrice': self.lastPrice,
            'lastQty': self.lastQty,
            'bidPrice': self.bidPrice,
            'bidQty': self.bidQty,
            'askPrice': self.askPrice,
            'askQty': self.askQty,
            'openPrice': self.openPrice,
            'highPrice': self.highPrice,
            'lowPrice': self.lowPrice,
            'volume': self.volume,
            'quoteVolume': self.quoteVolume,
            'openTime': self.openTime,
            'closeTime': self.closeTime,
            'firstId': self.firstId,
            'lastId': self.lastId,
            'count': self.count,
        }
