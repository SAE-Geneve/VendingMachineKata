from vending_machine import VendinMachine
from coin import Coin
from products_list import Products


class TestVendinMachineInit:
    def test_initial_balance_is_zero(self):
        vm = VendinMachine()
        assert vm.valueTotal == 0.0

    def test_initial_money_is_empty(self):
        vm = VendinMachine()
        assert vm.money == []

    def test_all_products_stocked_at_10(self):
        vm = VendinMachine()
        for name in Products:
            assert vm.products_number[name] == 10

    def test_all_products_present(self):
        vm = VendinMachine()
        assert set(vm.products_number.keys()) == set(Products.keys())


class TestInsertCoin:
    def test_insert_valid_coin_nickels(self):
        vm = VendinMachine()
        coin = Coin("nickels")
        vm.InsertCoin(coin)
        assert len(vm.money) == 1
        assert vm.money[0].value == 1.5

    def test_insert_valid_coin_dimes(self):
        vm = VendinMachine()
        coin = Coin("dimes")
        vm.InsertCoin(coin)
        assert len(vm.money) == 1

    def test_insert_valid_coin_quarters(self):
        vm = VendinMachine()
        coin = Coin("quarters")
        vm.InsertCoin(coin)
        assert len(vm.money) == 1

    def test_insert_pennies_rejected(self):
        vm = VendinMachine()
        coin = Coin("pennies")  # weight == 0.2, not > 0.2
        vm.InsertCoin(coin)
        assert len(vm.money) == 0

    def test_insert_invalid_coin_rejected(self):
        vm = VendinMachine()
        coin = Coin("fake")  # weight == 0.0
        vm.InsertCoin(coin)
        assert len(vm.money) == 0

    def test_insert_multiple_coins(self):
        vm = VendinMachine()
        vm.InsertCoin(Coin("nickels"))
        vm.InsertCoin(Coin("dimes"))
        vm.InsertCoin(Coin("quarters"))
        assert len(vm.money) == 3


class TestCalculeValue:
    def test_calcule_single_coin(self):
        vm = VendinMachine()
        vm.InsertCoin(Coin("nickels"))
        vm.CalculeValue()
        assert vm.valueTotal == 1.5

    def test_calcule_multiple_coins(self):
        vm = VendinMachine()
        vm.InsertCoin(Coin("nickels"))
        vm.InsertCoin(Coin("dimes"))
        vm.CalculeValue()
        assert vm.valueTotal == 2.5

    def test_calcule_no_coins(self):
        vm = VendinMachine()
        vm.CalculeValue()
        assert vm.valueTotal == 0.0


class TestCancel:
    def test_cancel_clears_money(self):
        vm = VendinMachine()
        vm.InsertCoin(Coin("nickels"))
        vm.InsertCoin(Coin("dimes"))
        vm.CalculeValue()
        vm.Cancel()
        assert vm.money == []
        assert vm.valueTotal == 0

    def test_cancel_when_empty(self):
        vm = VendinMachine()
        vm.Cancel()
        assert vm.money == []
        assert vm.valueTotal == 0


class TestRefillMachine:
    def test_refill_restores_stock(self):
        vm = VendinMachine()
        vm.products_number["Cola"] = 0
        vm.products_number["Chips"] = 3
        vm.RefillMachine()
        for name in Products:
            assert vm.products_number[name] == 10


class TestVoidMachine:
    def test_void_resets_balance(self):
        vm = VendinMachine()
        vm.InsertCoin(Coin("nickels"))
        vm.CalculeValue()
        vm.VoidMachine()
        assert vm.valueTotal == 0
