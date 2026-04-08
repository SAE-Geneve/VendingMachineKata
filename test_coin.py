from coin import Coin, type_coin


class TestCoinInit:
    def test_nickels(self):
        coin = Coin("nickels")
        assert coin.name == "nickels"
        assert coin.weight == 1.5
        assert coin.size == 1.5
        assert coin.value == 1.5

    def test_dimes(self):
        coin = Coin("dimes")
        assert coin.name == "dimes"
        assert coin.weight == 1.0
        assert coin.size == 1.0
        assert coin.value == 1.0

    def test_quarters(self):
        coin = Coin("quarters")
        assert coin.name == "quarters"
        assert coin.weight == 0.5
        assert coin.size == 0.5
        assert coin.value == 0.5

    def test_pennies(self):
        coin = Coin("pennies")
        assert coin.name == "pennies"
        assert coin.weight == 0.2
        assert coin.size == 0.2
        assert coin.value == 0.2

    def test_invalid_coin(self):
        coin = Coin("fake")
        assert coin.weight == 0.0
        assert coin.size == 0.0
        assert coin.value == 0.0


class TestTypeCoin:
    def test_type_coin_list(self):
        assert type_coin == ["nickels", "dimes", "quarters", "pennies"]

    def test_type_coin_length(self):
        assert len(type_coin) == 4
