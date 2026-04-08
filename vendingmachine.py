from coin import Coin, CoinType
from typing import List

class VendingMachine:
    def __init__(self):
        self._storage:List[Coin] = []

    def storage(self):
        return self._storage

    def basket(self):
        pass

    def insert_coin(self, first_coin, *args):
        coins = list(args) + [first_coin]
        self._storage.extend(coins)