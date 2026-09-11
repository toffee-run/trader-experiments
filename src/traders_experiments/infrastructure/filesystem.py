from obstore.store import LocalStore
from pandera.typing import DataFrame

from traders_experiments.domain.klines import Klines
from traders_experiments.domain.market import Market
from .binance_vision import BinanceVision


class FileSystem:
    def __init__(self):
        self.remote = BinanceVision()
        self.local = LocalStore()

    async def __call__(
        self, market: Market, base: str, quote: str
    ) -> DataFrame[Klines]:
        return await self.remote(market, base, quote)


__all__ = ("FileSystem",)
