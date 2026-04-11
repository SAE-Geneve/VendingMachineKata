from dataclasses import dataclass
from enum import Enum

class CoinType(Enum):
    PENNY = 1
    NICKEL = 2
    DIME = 3
    QUARTER = 4
    INVALID = 5

@dataclass
class CoinParameter:
    weight: int
    size: int
    value: float


class Coin:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size

    @staticmethod
    def create_penny():
        return Coin(1, 2)

    @staticmethod
    def create_dime():
        return Coin(1, 1)

    @staticmethod
    def create_nickel():
        return Coin(2, 1)

    @staticmethod
    def create_quarter():
        return Coin(2, 2)

    @staticmethod
    def create_coin(coin_type: CoinType):
        if coin_type not in coin_creation_map:
            raise ValueError("Invalid Coin")
        return coin_creation_map.get(coin_type)()

coin_creation_map = {
    CoinType.DIME: Coin.create_dime,
    CoinType.NICKEL: Coin.create_nickel,
    CoinType.PENNY: Coin.create_penny,
    CoinType.QUARTER: Coin.create_quarter
}