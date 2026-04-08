from enum import Enum


class Coin:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size

    @staticmethod
    def CreatePenny():
        return Coin(1, 5)

    @staticmethod
    def CreateNickel():
        return Coin(1, 5)

    @staticmethod
    def CreateDime():
        return Coin(1, 5)

    @staticmethod
    def CreateQuarter():
        return Coin(1, 5)

    @staticmethod
    def CreateCoin(coin: CoinType):
        if coin == CoinType.Penny:
            return Coin.CreatePenny()
        elif coin == CoinType.Nickel:
            return Coin.CreateNickel()
        elif coin == CoinType.Dime:
            return Coin.CreateDime()
        elif coin == Coin.CreateQuarter():
            return Coin.CreateQuarter()


class CoinType(Enum):
    Penny = 1
    Nickel = 2
    Dime = 3
    Quarter = 4
