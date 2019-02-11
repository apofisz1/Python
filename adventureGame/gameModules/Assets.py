class Item():
    def __init__(self):
        self.name = None
        self.price = 0
        self.currentHP = 100
        self.strengthModifier = 0
        self.HPmodifier = 0

    def create(self, name, price, strengthModifier, HPmodifier):
        self.name = name
        self.price = price
        self.strengthModifier = strengthModifier
        self.HPmodifier = HPmodifier

    def __str__(self):
        return "{}, {} golds".format(self.name, self.price)