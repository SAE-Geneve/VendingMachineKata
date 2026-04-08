import pytest
from vendingmachine import *
from coin import CoinType, Coin


def test_coin_insert():
    v=VendingMachine()
    dime=Coin.CreateCoin(CoinType.Dime)
    v.InsertCoin(dime)
    assert dime in v.CheckStorage()

def test_coin_insert_multiple():
    v=VendingMachine()
    coins=[]

    coins.append(Coin.CreateCoin(CoinType.Nickel))
    coins.append(Coin.CreateCoin(CoinType.Nickel))
    coins.append(Coin.CreateCoin(CoinType.Dime))

    for new_coin in coins:
        v.InsertCoin(new_coin)
    for new_coin in coins:
        assert new_coin in v.CheckStorage()

def test_coin_invalidity():
    v=VendingMachine()
    penny=Coin.CreateCoin(CoinType.Penny)
    v.InsertCoin(penny)

    assert penny not in v.CheckStorage()
    assert penny in v.CheckBasket()
    assert len(v.CheckStorage())==0