import pytest
from vendingmachine import *

def test_coin_insert(vending_machine):
    dime = Coin.CreateCoin(CoinType.Dime)
    vending_machine.InsertCoin(dime)
    assert dime in vending_machine.CheckStorage()

def test_coin_insert_multiple(vending_machine):
    coins = []

    coins.append(Coin.CreateCoin(CoinType.Dime))
    coins.append(Coin.CreateCoin(CoinType.Quarter))
    coins.append(Coin.CreateCoin(CoinType.Dime))

    for new_coin in coins:
        vending_machine.InsertCoin(new_coin)
    for new_coin in coins:
        assert new_coin in vending_machine.CheckStorage()


def test_coin_invalidity(vending_machine):
    penny = Coin.CreateCoin(CoinType.Penny)
    vending_machine.InsertCoin(penny)

    assert penny not in vending_machine.CheckStorage()
    assert penny in vending_machine.CheckBasket()
    assert len(vending_machine.CheckStorage()) == 0


@pytest.mark.parametrize("type_coin", [CoinType.Penny, CoinType.Dime, CoinType.Nickel, CoinType.Quarter])
def test_type_coin(type_coin):
    c = Coin.CreateCoin(type_coin)
    assert VendingMachine.GetTypeFromCoin(c) == type_coin

@pytest.fixture()
def vending_machine():
    return VendingMachine()