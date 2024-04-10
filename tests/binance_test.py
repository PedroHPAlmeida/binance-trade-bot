from unittest.mock import MagicMock

from pytest import fixture

from src.binance_api import Binance


@fixture
def binance():
    yield Binance(MagicMock())


def test_ping(binance):
    binance.ping()

    binance._client.ping.assert_called_once()
