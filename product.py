from dataclasses import dataclass
from enum import Enum

@dataclass()
class Product:
    price: float
    stock: int

class ProductType(Enum):
    Cola = 1
    Chips = 2
    Candy = 3