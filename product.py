from dataclasses import dataclass
from enum import Enum

@dataclass()
class ProductData:
    price: float
    stock: int
    type: ProductType

class ProductType(Enum):
    INVALID = 0
    COLA = 1
    CHIPS = 2
    CANDY = 3

class Product:
    def __init__(self, data: ProductData):
        self.data = data

    @staticmethod
    def create_product(product_type, stock):
        if product_type not in product_price_map:
            raise ValueError("Invalid Product")

        data = ProductData(product_price_map.get(product_type), stock, product_type)

        return Product(data)

product_price_map = {
    ProductType.COLA : 1,
    ProductType.CHIPS : 0.5,
    ProductType.CANDY : 0.65
}