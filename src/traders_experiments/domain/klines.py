from pandera.pandas import DataFrameModel
from pandera.typing import Series


class Klines(DataFrameModel):
    open: Series[float]
    high: Series[float]
    low: Series[float]
    close: Series[float]
    volume: Series[float]
