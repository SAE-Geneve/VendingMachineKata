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

product_price_map = {
    ProductType.Cola : 1,
    ProductType.Chips : 0.5,
    ProductType.Candy : 0.65
}