from coin import CoinType, Coin
from typing import List


class VendingMachine:
    def __init__(self):
        self.storage: List[Coin] = []
        self.coins_basket: List[Coin] = []
        self.total_money=0

    def InsertCoin(self, first_coin, *args):
        coins = list(args) + [first_coin]
        valid_coins = []

        for coin in coins:
            if VendingMachine.GetTypeFromCoin(coin) != CoinType.Penny:
                valid_coins.append(coin)
                match VendingMachine.GetTypeFromCoin(coin):
                    case CoinType.Nickel:
                        self.total_money+=5
                    case CoinType.Dime:
                        self.total_money+=10
                    case CoinType.Quarter:
                        self.total_money+=25
                    case _:
                        print("Invalid coin inserted however it was accepted")
            else:
                self.coins_basket.append(coin)

        self.storage.extend(valid_coins)

    def CheckStorage(self):
        return self.storage

    def CheckBasket(self):
        return self.coins_basket

    def MoneyTotal(self):
        return self.total_money

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
