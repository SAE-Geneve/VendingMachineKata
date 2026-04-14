from enum import Enum


class CoinType(Enum):
    Penny = 1
    Nickel = 2
    Dime = 3
    Quarter = 4
    Unrecognized = 5


class Coin:
    def __init__(self, weight, size, price):
        self.weight = weight
        self.size = size
        self.price = price


    def CoinValue(self):
        return self.price

    @staticmethod
    def CreatePenny():
        return Coin(1, 1, 1)

    @staticmethod
    def CreateNickel():
        return Coin(1, 2, 5)

    @staticmethod
    def CreateDime():
        return Coin(2, 1, 10)

    @staticmethod
    def CreateQuarter():
        return Coin(2, 2, 25)

    @staticmethod
    def CreateCoin(coin_type: CoinType):
        if coin_type not in dico:
            raise ValueError("Invalid coin")
        func = dico.get(coin_type)
        return func()


dico = {
    CoinType.Penny: Coin.CreatePenny,
    CoinType.Nickel: Coin.CreateNickel,
    CoinType.Dime: Coin.CreateDime,
    CoinType.Quarter: Coin.CreateQuarter
}
