from coin import Coin
from products_list import Products
from typing import List

class VendinMachine():
    def __init__(self):
        self.products_number = {}
        for p in Products:
            self.products_number[p] = 10
        self.money: List[Coin] = []
        self.valueTotal = 0.0
    
    def InsertCoin(self, coin: Coin):
        if coin.weight > 0.2 and coin.size > 0.2:
            self.money.append(coin)
            print("Add", coin.value)
        else:
            print("Invalide Money")
            
    def CalculeValue(self):
        self.valueTotal = sum(v.value for v in self.money)
        print(f"Total : ${self.valueTotal:.2f}")
        
    def Cancel(self):
        self.money.clear()
        self.valueTotal = 0

    def RefillMachine(self):
        self.products_number.clear
        for p in Products:
            self.products_number[p] = 10
            
    def VoidMachine(self):
        self.money.clear
        self.valueTotal = 0
        self.products_number.clear