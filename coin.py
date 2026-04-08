type_coin = ["nickels", "dimes", "quarters", "pennies"]

class Coin():
    def __init__(self, name: str):
        self.name = name
        if name == type_coin[0]:
            self.weight = 1.5
            self.size = 1.5
            self.value = 1.5
        elif name == type_coin[1]:
            self.weight = 1.0
            self.size = 1.0
            self.value = 1.0
        elif name == type_coin[2]:
            self.weight = 0.5
            self.size = 0.5
            self.value = 0.5
        elif name == type_coin[3]:
            self.weight = 0.2
            self.size = 0.2
            self.value = 0.2
        else:
            self.weight = 0.0
            self.size = 0.0
            self.value = 0.0