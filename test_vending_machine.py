import pytest

from product import product_price_map
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
    vending_machine.insert_coin(coin_quarter, coin_quarter, coin_quarter, coin_quarter) # 25 cents * 4 = $1.00

    assert vending_machine.inserted_coins_sum() == coin_quarter.data.value * 4

@pytest.mark.parametrize("type_coin", [CoinType.DIME, CoinType.NICKEL, CoinType.PENNY, CoinType.QUARTER])
def test_coin_type(type_coin: CoinType):
    coin = Coin.create_coin(type_coin)
    assert Coin.get_type_from_coin(coin) == type_coin

def test_add_storage(vending_machine_sold_out, coin_dime):
    vending_machine_sold_out.add_storage(coin_dime)
    assert coin_dime in vending_machine_sold_out.get_storage()

def test_create_product():
    product = Product.create_product(ProductType.CANDY, 1)
    assert product.data.type == ProductType.CANDY
    assert product.data.stock == 1

def test_get_product_from_type(vending_machine):
    product = vending_machine.get_product_from_type(ProductType.CANDY)
    assert product.data.type == ProductType.CANDY

def test_select_product_with_enough_coins(vending_machine, coin_quarter):
    vending_machine.insert_coin(coin_quarter, coin_quarter, coin_quarter, coin_quarter) # $1.00

    assert vending_machine.can_afford(ProductType.COLA) == True

    initial_stock = vending_machine.get_stock(ProductType.COLA) # $1.00
    initial_sum = vending_machine.get_storage_sum()

    vending_machine.select(ProductType.COLA)

    assert vending_machine.get_stock(ProductType.COLA) == initial_stock - 1
    assert coin_quarter in vending_machine.get_storage()
    assert vending_machine.get_storage_sum() == initial_sum + product_price_map.get(ProductType.COLA)
    assert len(vending_machine.get_inserted_coins()) == 0

def test_select_product_with_not_enough_coins(vending_machine, coin_quarter):
    vending_machine.insert_coin(coin_quarter, coin_quarter, coin_quarter) # $0.75

    assert vending_machine.can_afford(ProductType.COLA) == False

    initial_stock = vending_machine.get_stock(ProductType.COLA) # $1.00
    initial_storage_sum = vending_machine.get_storage_sum()

    vending_machine.select(ProductType.COLA)

    assert vending_machine.get_stock(ProductType.COLA) == initial_stock
    assert initial_storage_sum == vending_machine.get_storage_sum()

def test_select_product_exact_changes(vending_machine_sold_out, coin_quarter):
    vending_machine_sold_out.insert_coin(coin_quarter, coin_quarter, coin_quarter, coin_quarter, coin_quarter) # $1.25

    assert vending_machine_sold_out.can_afford(ProductType.COLA) == False

    initial_stock = vending_machine_sold_out.get_stock(ProductType.COLA)

    vending_machine_sold_out.select(ProductType.COLA)

    assert vending_machine_sold_out.get_stock(ProductType.COLA) == initial_stock

    vending_machine_sold_out.return_coins()
    vending_machine_sold_out.insert_coin(coin_quarter, coin_quarter, coin_quarter, coin_quarter) # $1.00

    vending_machine_sold_out.select(ProductType.COLA)

    assert vending_machine_sold_out.get_stock(ProductType.COLA) == initial_stock - 1


def test_select_product_out_of_stock(vending_machine_no_stock, coin_quarter):
    vending_machine_no_stock.insert_coin(coin_quarter, coin_quarter, coin_quarter, coin_quarter, coin_quarter) # $1.25

    assert vending_machine_no_stock.can_afford(ProductType.COLA) == False

    initial_storage_sum = vending_machine_no_stock.get_storage_sum()

    vending_machine_no_stock.select(ProductType.COLA)

    assert vending_machine_no_stock.get_storage_sum() == initial_storage_sum

def test_make_changes(vending_machine_sold_out, coin_quarter, coin_nickel, coin_dime):
    vending_machine_sold_out.insert_coin(coin_quarter, coin_quarter, coin_quarter, coin_nickel, coin_nickel, coin_nickel) # $1.05
    vending_machine_sold_out.add_storage(coin_dime)

    vending_machine_sold_out.select(ProductType.COLA)

    assert vending_machine_sold_out.get_storage_sum() == 1
    assert vending_machine_sold_out.inserted_coins_sum() == 0

@pytest.fixture
def vending_machine(coin_penny, coin_dime, coin_nickel, coin_quarter):
    vending_machine = VendingMachine()

    for i in range(10):
        vending_machine.add_storage(coin_penny, coin_dime, coin_nickel, coin_quarter)

    return vending_machine

@pytest.fixture
def vending_machine_no_stock(coin_penny, coin_dime, coin_nickel, coin_quarter):
    vending_machine = VendingMachine(0)

    for i in range(10):
        vending_machine.add_storage(coin_penny, coin_dime, coin_nickel, coin_quarter)

    return vending_machine

@pytest.fixture
def vending_machine_sold_out():
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