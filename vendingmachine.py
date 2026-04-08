from coin import CoinType, Coin
from typing import List

class VendingMachine:
    def __init__(self):
        self.total_money:float=0
        self.storage:List[Coin]=[]
        self.coins_basket:List[Coin]=[]

    def InsertCoin(self, first_coin: Coin, *args):
        coins=list(args)+[first_coin]
        #self.storage.extend(coins)

        if first_coin.weight == 1:
            self.coins_basket.append(first_coin)
            return
        else:
            self.storage.append(first_coin)
            self.total_money=first_coin.weight
            return

    def CheckStorage(self):
        return self.storage

    def CheckBasket(self):
        return self.coins_basket