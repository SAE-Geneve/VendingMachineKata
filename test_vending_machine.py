import pytest
from vending_machine import *
from coin import Coin

def test_coin_insert(vending_machine, coin_dime):
    vending_machine.insert_coin(coin_dime)
    assert coin_dime in vending_machine.get_inserted_coins()

def test_coin_insert_multiple(vending_machine, coin_dime, coin_nickel, coin_quarter):
    vending_machine.insert_coin(coin_dime, coin_nickel, coin_quarter)

    inserted_coins = vending_machine.get_inserted_coins()

    assert coin_dime in inserted_coins
    assert coin_nickel in inserted_coins
    assert coin_quarter in inserted_coins

def test_coin_invalidity(vending_machine, coin_penny):
    vending_machine.insert_coin(coin_penny)

    assert len(vending_machine.get_inserted_coins()) == 0

def test_return_coins(vending_machine, coin_penny, coin_dime):
    vending_machine.insert_coin(coin_penny, coin_dime)

    assert coin_dime in vending_machine.get_inserted_coins()
    assert coin_penny not in vending_machine.get_inserted_coins()

    vending_machine.return_coins()

    assert len(vending_machine.get_inserted_coins()) == 0

def test_inserted_coins_sum(vending_machine, coin_quarter):
    vending_machine.insert_coin(coin_quarter, coin_quarter, coin_quarter, coin_quarter) # 25 cents * 4 = 100

    assert vending_machine.inserted_coins_sum() == 100

@pytest.mark.parametrize("type_coin", [CoinType.DIME, CoinType.NICKEL, CoinType.PENNY, CoinType.QUARTER])
def test_coin_type(type_coin: CoinType):
    coin = Coin.create_coin(type_coin)
    assert Coin.get_type_from_coin(coin) == type_coin

@pytest.fixture
def vending_machine():
    return VendingMachine()

@pytest.fixture
def coin_penny():
    return Coin.create_coin(CoinType.PENNY)

@pytest.fixture
def coin_dime():
    return Coin.create_coin(CoinType.DIME)

@pytest.fixture
def coin_nickel():
    return Coin.create_coin(CoinType.NICKEL)

@pytest.fixture
def coin_quarter():
    return Coin.create_coin(CoinType.QUARTER)