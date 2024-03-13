from typing import Any, Dict
from datetime import datetime


class Trade24hData:
    def __init__(self, **kwargs):
        self.symbol: str = kwargs['symbol']
        self.priceChange = float(kwargs['priceChange'])
        self.priceChangePercent = float(kwargs['priceChangePercent'])
        self.weightedAvgPrice = float(kwargs['weightedAvgPrice'])
        self.prevClosePrice = float(kwargs['prevClosePrice'])
        self.lastPrice = float(kwargs['lastPrice'])
        self.lastQty = float(kwargs['lastQty'])
        self.bidPrice = float(kwargs['bidPrice'])
        self.bidQty = float(kwargs['bidQty'])
        self.askPrice = float(kwargs['askPrice'])
        self.askQty = float(kwargs['askQty'])
        self.openPrice = float(kwargs['openPrice'])
        self.highPrice = float(kwargs['highPrice'])
        self.lowPrice = float(kwargs['lowPrice'])
        self.volume = float(kwargs['volume'])
        self.quoteVolume = float(kwargs['quoteVolume'])
        self.openTime = int(kwargs['openTime'])
        self.closeTime = int(kwargs['closeTime'])
        self.firstId = int(kwargs['firstId'])
        self.lastId = int(kwargs['lastId'])
        self.count = int(kwargs['count'])
        self.timestamp = datetime.now().isoformat()

    def as_dict(self) -> Dict[str, Any]:
        return self.__dict__

    def __str__(self) -> str:
        return str(self.__dict__)
