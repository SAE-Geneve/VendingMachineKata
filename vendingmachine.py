from coin import Coin, CoinType
from typing import List

class VendingMachine:
    def __init__(self):
        self._storage:List[Coin] = []
        self._basket:List[Coin] = []

    def storage(self):
        return self._storage

    def basket(self):
        return self._basket

    def insert_coin(self, first_coin:Coin, *args:Coin):
        coins = list(args) + [first_coin]
        valid_coins:List[Coin] = []
        invalid_coins:List[Coin] = []
        for coin in coins:
            if VendingMachine.get_coin_type(coin) != CoinType.Penny:
                valid_coins.append(coin)
            else :
                invalid_coins.append(coin)
        self._storage.extend(valid_coins)
        self._basket.extend(invalid_coins)

    @staticmethod
    def get_coin_type(coin: Coin):
        if coin.weight == 1 and coin.size == 1:
            return CoinType.Penny
        if coin.weight == 1 and coin.size == 2:
            return CoinType.Nickel
        if coin.weight == 2 and coin.size == 1:
            return CoinType.Dime
        if coin.weight == 2 and coin.size == 2:
            return CoinType.Quarter
        return None