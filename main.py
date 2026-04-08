from coin import Coin
from product import Products

if __name__ == '__main__':
    penny = Coin.CreatePenny()
    dime = Coin(1, 5)
    quarter = Coin(1, 5)

    print(penny.weight, " ",penny.size)
