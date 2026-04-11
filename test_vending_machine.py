import pytest
from vending_machine import *
from coin import Coin

def test_coin_insert(vending_machine):
    dime = Coin.create_coin(CoinType.DIME)
    vending_machine.insert_coin(dime)
    assert dime in vending_machine.get_inserted_coins()

def test_coin_insert_multiple(vending_machine):
    dime = Coin.create_coin(CoinType.DIME)
    nickel = Coin.create_coin(CoinType.NICKEL)
    quarter = Coin.create_coin(CoinType.QUARTER)

    vending_machine.insert_coin(dime, nickel, quarter)

    storage = vending_machine.get_inserted_coins()

    assert dime in storage
    assert nickel in storage
    assert quarter in storage

def test_coin_invalidity(vending_machine):
    penny = Coin.create_coin(CoinType.PENNY)

    vending_machine.insert_coin(penny)

    assert len(vending_machine.get_inserted_coins()) == 0

def test_return_coins(vending_machine):
    penny = Coin.create_coin(CoinType.PENNY)
    dime = Coin.create_coin(CoinType.DIME)

    vending_machine.insert_coin(penny, dime)

    assert penny, dime in vending_machine.get_inserted_coins()

    vending_machine.return_coins()

    assert len(vending_machine.get_inserted_coins()) == 0

def test_inserted_coins_sum(vending_machine):
    quarter = Coin.create_coin(CoinType.QUARTER) # 25 cents

    vending_machine.insert_coin(quarter, quarter, quarter, quarter)

    assert vending_machine.inserted_coins_sum() == 100

@pytest.mark.parametrize("type_coin", [CoinType.DIME, CoinType.NICKEL, CoinType.PENNY, CoinType.QUARTER])
def test_coin_type(type_coin: CoinType):
    coin = Coin.create_coin(type_coin)
    assert Coin.get_type_from_coin(coin) == type_coin

@pytest.fixture
def vending_machine():
    return VendingMachine()