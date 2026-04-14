from dataclasses import dataclass
from enum import Enum

class CoinType(Enum):
    PENNY = 1
    NICKEL = 2
    DIME = 3
    QUARTER = 4
    INVALID = 5

@dataclass
class CoinData:
    weight: int
    size: int
    value: float

class Coin:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def create_coin(coin_type: CoinType):
        if coin_type not in coin_parameter_map:
            raise ValueError("Invalid Coin")
        return Coin(coin_parameter_map.get(coin_type))

    @staticmethod
    def get_type_from_coin(coin: Coin):
        for key, param in coin_parameter_map.items():
            if param == coin.data:
                return key
        return CoinType.INVALID

coin_parameter_map = {
    CoinType.PENNY: CoinData(1, 1, 1),
    CoinType.DIME: CoinData(1, 2, 5),
    CoinType.NICKEL: CoinData(2, 1, 10),
    CoinType.QUARTER: CoinData(2, 2, 25)
}