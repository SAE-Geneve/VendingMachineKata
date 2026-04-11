from coin import Coin, CoinType
from typing import List

class VendingMachine:
    def __init__(self):
        self.storage:List[Coin] = []
        self.basket:List[Coin] = []

    def insert_coin(self, first_coin, *args):
        coins = list(args) + [first_coin]
        valid_coins = []
        for c in coins:
            if Coin.get_type_from_coin(c) != CoinType.PENNY:
                valid_coins.append(c)
            else:
                self.basket.append(c)

        self.storage.extend(valid_coins)

    def get_storage(self):
        return self.storage

    def get_basket(self):
        return self.basket