from products_list import Products

class Produt():
    def __init__(self, name: str):
        self.name = name
        for p in Products:
            if self.name == p:
                self.value = Products[p]
                return
        print("Product Not Existe")
