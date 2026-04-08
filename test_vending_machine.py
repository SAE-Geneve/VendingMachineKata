import pytest
from vending_machine import *

def test_coin_insert(vending_machine):
    d = Coin.create_coin(CoinType.DIME)
    vending_machine.insert_coin(d)
    assert d in vending_machine.get_storage()

def test_coin_insert_multiple(vending_machine):
    d = Coin.create_coin(CoinType.DIME)
    n = Coin.create_coin(CoinType.NICKEL)
    q = Coin.create_coin(CoinType.QUARTER)

    vending_machine.insert_coin(d)
    vending_machine.insert_coin(n)
    vending_machine.insert_coin(q)

    storage = vending_machine.get_storage()

    assert d in storage
    assert n in storage
    assert q in storage

def test_coin_invalidity(vending_machine):
    p = Coin.create_coin(CoinType.PENNY)

    vending_machine.insert_coin(p)

    assert len(vending_machine.get_storage()) == 0
    assert p in vending_machine.get_basket()

@pytest.mark.parametrize("type_coin", [CoinType.DIME, CoinType.NICKEL, CoinType.PENNY, CoinType.QUARTER])
def test_coin_type(type_coin: CoinType):
    c = Coin.create_coin(type_coin)
    assert VendingMachine.get_type_from_coin(c) == type_coin

@pytest.fixture
def vending_machine():
    return VendingMachine()