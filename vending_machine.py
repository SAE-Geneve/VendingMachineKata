from coin import Coin, CoinType
from typing import List

class VendingMachine:
    def __init__(self):
        self.inserted_coins:List[Coin] = []
        # self.basket:List[Coin] = []

    def insert_coin(self, first_coin, *args):
        coins = list(args) + [first_coin]
        valid_coins = []
        for c in coins:
            if Coin.get_type_from_coin(c) != CoinType.PENNY:
                valid_coins.append(c)
        self.inserted_coins.extend(valid_coins)

    def inserted_coins_sum(self):
        coins_sum = 0
        for coin in self.inserted_coins:
            coins_sum += coin.coin_parameter.value

        return coins_sum

    def return_coins(self):
        self.inserted_coins.clear()

    def get_inserted_coins(self):
        return self.inserted_coins