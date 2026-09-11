import ccxt.async_support as ccxt
from pandera.typing import DataFrame

from traders_experiments.domain.klines import Klines
from traders_experiments.domain.market import Market, Futures, SettlementEnum


class Binance:
    def __init__(self):
        self.client = ccxt.binance({'enableRateLimit': True})

    async def __aenter__(self):
        await self.client.load_markets()
        return self

    async def __call__(
        self, market: Market, base: str, quote: str, limit: int
    ) -> DataFrame[Klines]:
        symbol = f"{base}/{quote}"

        match market:
            case Futures(settlement=SettlementEnum.INVERSE):
                symbol += f":{base}"
            case Futures(settlement=SettlementEnum.LINEAR):
                symbol += f":{quote}"

        dataframe = {
            "open": [],
            "high": [],
            "low": [],
            "close": [],
            "volume": [],
        }

        for _, o, h, l, c, v in await self.client.fetch_ohlcv(symbol=symbol, timeframe="1m", limit=limit):
            dataframe["open"].append(o)
            dataframe["high"].append(h)
            dataframe["low"].append(l)
            dataframe["close"].append(c)
            dataframe["volume"].append(v)

        return DataFrame[Klines](dataframe)

    async def __aexit__(self, *exc):
        await self.client.close()


__all__ = ("Binance",)
