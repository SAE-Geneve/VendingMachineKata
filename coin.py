from dataclasses import dataclass
from enum import Enum

class CoinType(Enum):
    INVALID = 0
    PENNY = 1
    NICKEL = 2
    DIME = 3
    QUARTER = 4

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
        if coin_type not in coin_data_map:
            raise ValueError("Invalid Coin")
        return Coin(coin_data_map.get(coin_type))

    @staticmethod
    def get_type_from_coin(coin: Coin):
        for key, param in coin_data_map.items():
            if param == coin.data:
                return key
        return CoinType.INVALID

coin_data_map = {
    CoinType.PENNY: CoinData(1, 1, 0.01),
    CoinType.DIME: CoinData(1, 2, 0.05),
    CoinType.NICKEL: CoinData(2, 1, 0.1),
    CoinType.QUARTER: CoinData(2, 2, 0.25)
}