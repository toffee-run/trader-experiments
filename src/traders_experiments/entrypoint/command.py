import asyncio

from typer import Typer

from traders_experiments.infrastructure.binance import Binance
from traders_experiments.domain.market import Futures


import pandas as pd

pd.set_option('display.max_rows', None)


app = Typer()

async def abc():
    async with Binance() as binance:
        return await binance(Futures(), "BTC", "USDT", 100)

@app.command()
def check():
    print(asyncio.run(abc()))

__all__ = ("app",)
