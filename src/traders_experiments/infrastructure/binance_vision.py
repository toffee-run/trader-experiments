from obstore.store import S3Store
from pandera.typing import DataFrame

from traders_experiments.domain.klines import Klines
from traders_experiments.domain.market import Market


class BinanceVision:
    def __init__(self):
        self.client = S3Store()

    async def __call__(
        self, market: Market, base: str, quote: str
    ) -> DataFrame[Klines]: ...


__all__ = ("BinanceVision",)
