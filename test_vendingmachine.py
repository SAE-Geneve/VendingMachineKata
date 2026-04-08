import pytest
from vendingmachine import *
from coin import *
from product import *

@pytest.fixture
def vending_machine():
    return VendingMachine()

def test_insert_valid_coin(vending_machine):
    nickel = Coin.create_nickel()
    vending_machine.insert_coin(nickel)

    assert nickel in vending_machine.storage()

def test_insert_invalid_coin(vending_machine):
    penny = Coin.create_penny()
    vending_machine.insert_coin(penny)

    assert penny not in vending_machine.storage()
    assert penny in vending_machine.basket()
    assert len(vending_machine.storage()) == 0

def test_insert_multiple_coins(vending_machine):
    nickel = Coin.create_nickel()
    nickel2 = Coin.create_nickel()
    dime = Coin.create_dime()

    vending_machine.insert_coin(nickel, nickel2, dime)

    s = vending_machine.storage()

    assert nickel in s
    assert nickel2 in s
    assert dime in s

@pytest.mark.parametrize("coin_type", [CoinType.Penny, CoinType.Nickel, CoinType.Dime, CoinType.Quarter])
def test_coin_type(coin_type):
    coin = Coin.create_coin(coin_type)
    assert VendingMachine.get_coin_type(coin) == coin_type

