from enum import Enum

class CoinType(Enum):
    PENNY = 1
    NICKEL = 2
    DIME = 3
    QUARTER = 4
    INVALID = 5

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
        if coin_type not in dico:
            raise ValueError("Invalid Coin")
        func = dico.get(coin_type)
        return func()

dico = {
    CoinType.DIME: Coin.create_dime,
    CoinType.NICKEL: Coin.create_nickel,
    CoinType.PENNY: Coin.create_penny,
    CoinType.QUARTER: Coin.create_quarter
}