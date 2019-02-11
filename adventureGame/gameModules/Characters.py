import random

# base classes ************************
class Character():
    """
    Base class for all characters in the game.
    """

    def __init__(self):
        self.name = None
        self.characterClass = None
        self.gender = None
        self.age = None

        self.maxHP = 100
        self.currentHP = self.maxHP

        self.strength = 10
        self.inventory = []
        self.gold = 0

    def getStats(self, nice=False):
        statDict = {"name":self.name,
                    "characterClass":self.characterClass,
                    "maxHP":self.maxHP,
                    "currentHP":self.currentHP,
                    "gold":self.gold,
                    "strength":self.strength}

        if nice:
            print "-"*50
            for k, v in statDict.items():
                print k, v
            print "-" * 50

    def getInventory(self):
        print "Your inventory:"
        for i in self.inventory:
            print "\t", i

    def create(self, name, characterClass, gender, age):
        self.name = name
        self.characterClass = characterClass
        self.gender = gender
        self.age = age

        # setup attributes based on characterClass

        if characterClass == "human":
            self.maxHP = 150
            self.strength =35

        elif characterClass == "ork":
            self.maxHP = 300
            self.strength = 80

        elif characterClass == "mage":
            self.maxHP = 200
            self.strength = 25

        elif characterClass == "elf":
            self.maxHP = 200
            self.strength = 40

        self.gold = random.randint(10, 60)
        self.currentHP = self.maxHP

    def attack(self, enemy):
        attackStrength = random.randint(0, self.strength)

        enemy.setCurrentHP(attackStrength)

        print "{} attacks {}".format(self.name, enemy.name)
        print "{0} {1}HP \t {2} {3} HP".format(self.name, self.currentHP,
                                               enemy.name, enemy.currentHP)

    def setCurrentHP(self, valu):
        self.currentHP -= valu

    def buy(self, item):
        self.inventory.append(item)
        self.gold -= item.price

        self.strength += item.strengthModifier
        self.maxHP += item.HPmodifier
        self.currentHP = self.maxHP

    def sell(self):
        pass

    def __str__(self):
        return "{} {}".format(self.name, self.characterClass)

# base classes ***********************



class Player(Character):
    def __init__(self):
        Character.__init__(self)

class Enemy(Character):
    def __init__(self):
        Character.__init__(self)

class NPC(Character):
    def __init__(self):
        Character.__init__(self)

    def checkItem(self, character, item):

        if item.price > character.gold:
            return False

        return True