import pytest
from vendingmachine import *
from coin import *
from product import *

def test_insert_valid_coin():
    v = VendingMachine()

    nickel = Coin.create_nickel()
    v.insert_coin(nickel)

    assert nickel in v.storage()

def test_insert_invalid_coin():
    v = VendingMachine()

    penny = Coin.create_penny()
    v.insert_coin(penny)

    assert penny not in v.storage()
    assert penny in v.basket()
    assert len(v.storage()) == 0

def test_insert_multiple_coins():
    v = VendingMachine()

    nickel = Coin.create_nickel()
    nickel2 = Coin.create_nickel()
    dime = Coin.create_dime()

    v.insert_coin(nickel, nickel2, dime)

    s = v.storage()

    assert nickel in s
    assert nickel2 in s
    assert dime in s