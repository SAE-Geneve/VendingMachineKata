import pytest
from vendingmachine import *
from coin import CoinType, Coin


def test_coin_insert():
    v=VendingMachine()
    dime=Coin.CreateCoin(CoinType.Dime)
    v.InsertCoin(dime)
    assert dime in v.CheckStorage()

def test_coin_validity():
    assert True