from coin import Coin, CoinType
from typing import List

from product import Product, ProductType


class VendingMachine:
    def __init__(self, initial_stock = 10):
        self.inserted_coins:List[Coin] = []
        self.storage:List[Coin] = []
        self.products = [
            Product.create_product(ProductType.Cola, initial_stock),
            Product.create_product(ProductType.Chips, initial_stock),
            Product.create_product(ProductType.Candy, initial_stock)
        ]

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
            coins_sum += coin.data.value

        return coins_sum

    def return_coins(self):
        self.inserted_coins.clear()

    def get_inserted_coins(self):
        return self.inserted_coins

    def add_storage(self, first_coin, *args):
        self.storage.extend(list(args) + [first_coin])

    def get_storage_sum(self):
        coins_sum = 0
        for coin in self.storage:
            coins_sum += coin.data.value

        return coins_sum

    def select(self, product_type: ProductType):
        for product in self.products:
            data = product.data

            if product_type != data.type:
                continue

            coins_sum = self.inserted_coins
            if coins_sum >= data.price:
                data.stock -= 1

            break