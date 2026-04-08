import pytest
from vending_machine import *

def test_coin_insert():
    v = VendingMachine()
    d = Coin.create_coin(CoinType.DIME)
    v.insert_coin(d)
    assert d in v.get_storage()

def test_coin_insert_multiple():
    v = VendingMachine()
    d = Coin.create_coin(CoinType.DIME)
    n = Coin.create_coin(CoinType.NICKEL)
    q = Coin.create_coin(CoinType.QUARTER)

    v.insert_coin(d)
    v.insert_coin(n)
    v.insert_coin(q)

    storage = v.get_storage()

    assert d in storage
    assert n in storage
    assert q in storage

def test_coin_invalidity():
    v = VendingMachine()
    p = Coin.create_coin(CoinType.PENNY)

    v.insert_coin(p)

    assert len(v.get_storage()) == 0
    assert p in v.basket()

@pytest.mark.parametrize("type_coin", [CoinType.DIME, CoinType.NICKEL, CoinType.PENNY, CoinType.QUARTER])
def test_coin_type(type_coin: CoinType):
    c = Coin.create_coin(type_coin)
    assert VendingMachine.get_type_from_coin(c) == type_coin