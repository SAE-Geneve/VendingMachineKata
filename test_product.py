from product import Produt


class TestProdutInit:
    def test_valid_product_cola(self):
        p = Produt("Cola")
        assert p.name == "Cola"
        assert p.value == 1.0

    def test_valid_product_chips(self):
        p = Produt("Chips")
        assert p.name == "Chips"
        assert p.value == 0.5

    def test_valid_product_sandwich(self):
        p = Produt("Sandwich")
        assert p.name == "Sandwich"
        assert p.value == 3.5

    def test_valid_product_coffee(self):
        p = Produt("Coffee")
        assert p.name == "Coffee"
        assert p.value == 2.0

    def test_invalid_product_has_no_value(self):
        p = Produt("Unknown")
        assert p.name == "Unknown"
        assert not hasattr(p, "value")
