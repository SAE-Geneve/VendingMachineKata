import pytest
from vending_machine import *
from coin import Coin

def test_coin_insert(vending_machine):
    dime = Coin.create_coin(CoinType.DIME)
    vending_machine.insert_coin(dime)
    assert dime in vending_machine.get_storage()

def test_coin_insert_multiple(vending_machine):
    dime = Coin.create_coin(CoinType.DIME)
    nickel = Coin.create_coin(CoinType.NICKEL)
    quarter = Coin.create_coin(CoinType.QUARTER)

    vending_machine.insert_coin(dime, nickel, quarter)

    storage = vending_machine.get_storage()

    assert dime in storage
    assert nickel in storage
    assert quarter in storage

def test_coin_invalidity(vending_machine):
    penny = Coin.create_coin(CoinType.PENNY)

    vending_machine.insert_coin(penny)

    assert len(vending_machine.get_storage()) == 0
    assert penny in vending_machine.get_basket()

def test_storage_sum(vending_machine):
    coin = Coin.create_coin(CoinType.QUARTER)

    vending_machine.insert_coin(coin, coin, coin, coin)

    assert vending_machine.storage_sum() == 100

@pytest.mark.parametrize("type_coin", [CoinType.DIME, CoinType.NICKEL, CoinType.PENNY, CoinType.QUARTER])
def test_coin_type(type_coin: CoinType):
    coin = Coin.create_coin(type_coin)
    assert Coin.get_type_from_coin(coin) == type_coin

@pytest.fixture
def vending_machine():
    return VendingMachine()