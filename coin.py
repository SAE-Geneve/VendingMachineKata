from enum import Enum

class CoinType(Enum):
    Penny = 1
    Nickel = 2
    Dime = 3
    Quarter = 4
    Invalid = 5

class Coin:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size
    @staticmethod
    def create_penny():
        return Coin(1, 1)
    @staticmethod
    def create_nickel():
        return Coin(1, 2)
    @staticmethod
    def create_dime():
        return Coin(2, 1)
    @staticmethod
    def create_quarter():
        return Coin(2, 2)
    @staticmethod
    def create_coin(coin_type: CoinType):
        if coin_type not in dico:
            raise ValueError("Invalid Coin type")
        func = dico.get(coin_type)
        return func()

dico = {
    CoinType.Penny: Coin.create_penny,
    CoinType.Nickel: Coin.create_nickel,
    CoinType.Dime: Coin.create_dime,
    CoinType.Quarter: Coin.create_quarter
}