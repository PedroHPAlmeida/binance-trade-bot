from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class MyCoin:
    asset: str
    free: float
    locked: float

    def __post_init__(self):
        self.free = float(self.free)
        self.locked = float(self.locked)

    def as_dict(self) -> Dict[str, Any]:
        return {"asset": self.asset, "free": self.free, "locked": self.locked}
