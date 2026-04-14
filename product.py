from dataclasses import dataclass
from enum import Enum

@dataclass()
class ProductData:
    price: float
    stock: int
    type: ProductType

class ProductType(Enum):
    Cola = 1
    Chips = 2
    Candy = 3

class Product:
    def __init__(self, data: ProductData):
        self.data = data

    @staticmethod
    def create_product(product_type, stock):
        if product_type not in product_price_map:
            raise ValueError("Invalid Product")

        product = ProductData
        product.price = product_price_map.get(product_type)
        product.stock = stock
        product.type = product_type

        return Product(product)

product_price_map = {
    ProductType.Cola : 1,
    ProductType.Chips : 0.5,
    ProductType.Candy : 0.65
}