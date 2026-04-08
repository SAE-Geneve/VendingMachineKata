from coin import Coin, CoinType
from product import Product
from vending_machine import VendingMachine


if __name__ == '__main__':
    penny = Coin.create_coin(CoinType.Penny)
    nickel = Coin.create_coin(CoinType.Nickel)
    dime = Coin.create_coin(CoinType.Dime)
    quarter = Coin.create_coin(CoinType.Quarter)

    print(penny.weight, penny.size)
    print(nickel.weight, nickel.size)
    print(dime.weight, dime.size)
    print(quarter.weight, quarter.size)