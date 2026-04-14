from coin import Coin, CoinType, coin_data_map
from typing import List

from product import Product, ProductType


class VendingMachine:
    def __init__(self, initial_stock = 10):
        self.inserted_coins:List[Coin] = []
        self.storage:List[Coin] = []
        self.products:List[Product] = []
        self.products.append(Product.create_product(ProductType.COLA, initial_stock))
        self.products.append(Product.create_product(ProductType.CHIPS, initial_stock))
        self.products.append(Product.create_product(ProductType.CANDY, initial_stock))


    def insert_coin(self, first_coin, *args):
        coins = list(args) + [first_coin]
        valid_coins = []
        for c in coins:
            if Coin.get_type_from_coin(c) != CoinType.PENNY:
                valid_coins.append(c)
        self.inserted_coins.extend(valid_coins)

    @staticmethod
    def coins_sum(coins: List[Coin]):
        coins_sum = 0
        for coin in coins:
            coins_sum += coin.data.value

        return coins_sum
    def inserted_coins_sum(self):
        return VendingMachine.coins_sum(self.inserted_coins)

    def return_coins(self):
        self.inserted_coins.clear()

    def get_inserted_coins(self):
        return self.inserted_coins

    def add_storage(self, first_coin, *args):
        self.storage.extend(list(args) + [first_coin])

    def get_storage(self):
        return self.storage

    def get_storage_sum(self):
        return VendingMachine.coins_sum(self.storage)

    def get_stock(self, product_type: ProductType):
        return self.get_product_from_type(product_type).data.stock

    def can_afford(self, product_type):
        product = self.get_product_from_type(product_type)
        data = product.data

        if data.stock == 0:
            return False

        inserted_sum = self.inserted_coins_sum()
        price = data.price

        if inserted_sum < price:
            return False

        # Changes
        change_sum = inserted_sum - price
        current_sum = change_sum
        change_coins:List[Coin] = []

        quarter = coin_data_map.get(CoinType.QUARTER)
        nickel = coin_data_map.get(CoinType.NICKEL)
        dime = coin_data_map.get(CoinType.DIME)
        penny = coin_data_map.get(CoinType.PENNY)

        while current_sum >= quarter.value and quarter in self.storage:
            change_coins.append(quarter)
            current_sum -= quarter.value

        while current_sum >= nickel.value and nickel in self.storage:
            change_coins.append(nickel)
            current_sum -= nickel.value

        while current_sum >= dime.value and dime in self.storage:
            change_coins.append(dime)
            current_sum -= dime.value

        while current_sum >= penny.value and penny in self.storage:
            change_coins.append(penny)
            current_sum -= penny.value

        return VendingMachine.coins_sum(change_coins) == change_sum
    def get_product_from_type(self, product_type: ProductType):
        for product in self.products:
            if product.data.type == product_type:
                return product
        raise ValueError("Invalid Product")

    def select(self, product_type: ProductType):
        pass