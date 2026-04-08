from enum import Enum

class CoinType(Enum):
    PENNY = 1
    NICKEL = 2
    DIME = 3
    QUARTER = 4

class Coin:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size

    @staticmethod
    def create_penny():
        return Coin(1, 5)

    @staticmethod
    def create_dime():
        return Coin(1, 5)

    @staticmethod
    def create_nickel():
        return Coin(1, 5)

    @staticmethod
    def create_quarters():
        return Coin(1, 5)

    @staticmethod
    def create_coin(type: CoinType):
        if type == CoinType.PENNY:
            return Coin.create_penny()
        elif type == CoinType.DIME:
            return Coin.create_dime()
        elif type == CoinType.NICKEL:
            return Coin.create_nickel()
        else:
            return Coin.create_quarters()