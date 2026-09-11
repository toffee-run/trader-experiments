from typing import Literal, Annotated
from enum import StrEnum, auto

from pydantic import BaseModel, Field


class MarketEnum(StrEnum):
    SPOT = auto()
    FUTURES = auto()


class Spot(BaseModel):
    market: Literal[MarketEnum.SPOT] = MarketEnum.SPOT


class SettlementEnum(StrEnum):
    LINEAR = auto()
    INVERSE = auto()


class Futures(BaseModel):
    market: Literal[MarketEnum.FUTURES] = MarketEnum.FUTURES
    settlement: SettlementEnum = SettlementEnum.LINEAR


Market = Annotated[Spot | Futures, Field(discriminator="market")]

__all__ = ("MarketEnum", "Spot", "SettlementEnum", "Futures", "Market")
