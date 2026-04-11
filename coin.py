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
    def __init__(self, coin_parameter):
        self.coin_parameter = coin_parameter

    @staticmethod
    def create_penny():
        return Coin(coin_parameter_map.get(CoinType.PENNY))

    @staticmethod
    def create_dime():
        return Coin(coin_parameter_map.get(CoinType.DIME))

    @staticmethod
    def create_nickel():
        return Coin(coin_parameter_map.get(CoinType.NICKEL))

    @staticmethod
    def create_quarter():
        return Coin(coin_parameter_map.get(CoinType.QUARTER))

    @staticmethod
    def create_coin(coin_type: CoinType):
        if coin_type not in coin_creation_map:
            raise ValueError("Invalid Coin")
        return coin_creation_map.get(coin_type)()

coin_parameter_map = {
    CoinType.PENNY: CoinParameter(1, 1, 1),
    CoinType.DIME: CoinParameter(1, 2, 5),
    CoinType.NICKEL: CoinParameter(2, 1, 10),
    CoinType.QUARTER: CoinParameter(2, 2, 25)
}


coin_creation_map = {
    CoinType.DIME: Coin.create_dime,
    CoinType.NICKEL: Coin.create_nickel,
    CoinType.PENNY: Coin.create_penny,
    CoinType.QUARTER: Coin.create_quarter
}