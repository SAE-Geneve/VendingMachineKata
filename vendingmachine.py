from coin import CoinType, Coin
from typing import List


class VendingMachine:
    def __init__(self):
        self.storage: List[Coin] = []
        self.coins_basket: List[Coin] = []

    def InsertCoin(self, first_coin, *args):
        coins = list(args) + [first_coin]
        valid_coins = []

        for c in coins:
            if VendingMachine.GetTypeFromCoin(c) != CoinType.Penny:
                valid_coins.append(c)
            else:
                self.coins_basket.append(c)

        self.storage.extend(valid_coins)

    def CheckStorage(self):
        return self.storage

    def CheckBasket(self):
        return self.coins_basket

    @staticmethod
    def GetTypeFromCoin(coin: Coin):
        if coin.weight == 1 and coin.size == 1:
            return CoinType.Penny
        elif coin.weight == 1 and coin.size == 2:
            return CoinType.Nickel
        elif coin.weight == 2 and coin.size == 1:
            return CoinType.Dime
        elif coin.weight == 2 and coin.size == 2:
            return CoinType.Quarter
        return None
