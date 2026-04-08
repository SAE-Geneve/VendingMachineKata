from timeit import default_timer

import pytest
from coin import *
from vendingmachine import *
def test_valid_coin_insert():
    v = VendingMachine()

    nickel = Coin.create_nickel()
    v.InsertCoin(nickel)

    s = v.CheckStorage()

    assert nickel in s

def test_invalid_coin_insert():
    v = VendingMachine()
    v.InsertCoin(CoinType.Penny)

    assert CoinType.Penny not in v.CheckStorage()
