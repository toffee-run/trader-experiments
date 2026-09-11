import ccxt.async_support as ccxt
from pandera.typing import DataFrame

from traders_experiments.domain.klines import Klines
from traders_experiments.domain.market import Market


class Bybit:
    def __init__(self):
        self.client = ccxt.bybit({'enableRateLimit': True})

    async def __call__(
        self, market: Market, base: str, quote: str, limit: int
    ) -> DataFrame[Klines]: ...


__all__ = ("Bybit",)
