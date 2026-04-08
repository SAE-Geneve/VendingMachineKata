from enum import Enum

class CoinType(Enum):
    Penny = 1
    Nickel = 2
    Dime = 3
    Quarter = 4

class Coin:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size

    @staticmethod
    def create_penny():
        return Coin(1, 5)
    @staticmethod
    def create_nickel():
        return Coin(2, 10)
    @staticmethod
    def create_dime():
        return Coin(3, 15)
    @staticmethod
    def create_quarter():
        return Coin(4, 20)
    @staticmethod
    def create_coin(coin:CoinType):
        if coin == CoinType.Penny:
            return Coin.create_penny()
        elif coin == CoinType.Nickel:
            return Coin.create_nickel()
        elif coin == CoinType.Dime:
            return Coin.create_dime()
        elif coin == CoinType.Quarter:
            return Coin.create_quarter()
