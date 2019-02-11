import Characters, Assets
import time

class Arena():
    def __init__(self, Game):
        self.Game = Game

        self.enemies = []
        self.createEnemies()

        self.master = Characters.NPC()
        self.master.create("Truz", "ork", "man", 79)

    def createEnemies(self):
        # name, characterClass, gender, age
        enemy1 = Characters.Enemy()
        enemy1.create("Sauron", "mage", "male", "860")

        enemy2 = Characters.Enemy()
        enemy2.create("Zork", "ork", "male", "68")

        enemy3 = Characters.Enemy()
        enemy3.create("Gilda", "elf", "male", "180")


        self.enemies.append(enemy1)
        self.enemies.append(enemy2)
        self.enemies.append(enemy3)

    def menu(self):
        self.Game.clearWindow()
        print "Hello {}. I'm {}. Choose your enemy!".format(self.Game.player.name, self.master.name)

        for index, item in enumerate(self.enemies):
            print index, item

        backMenu = index + 1
        print backMenu, "Back to Main Menu"

        userInput = raw_input()

        if userInput == str(backMenu):
            self.Game.menu()

        enemy = self.enemies[int(userInput)]
        self.fight(enemy)

    def fight(self, enemy):
        self.Game.clearWindow()
        print "{} vs. {}".format(self.Game.player.name, enemy.name)
        time.sleep(3)

        winner = None
        while True:
            self.Game.clearWindow()
            self.Game.player.attack(enemy)

            if enemy.currentHP <= 0:
                winner = self.Game.player
                break
            # time.sleep(3)

            self.Game.clearWindow()
            enemy.attack(self.Game.player)
            if self.Game.player.currentHP <= 0:
                winner = enemy
                break

            # time.sleep(3)

        print "Winner is: {}".format(winner.name)

class Shop():
    def __init__(self, Game):
        self.Game = Game

        self.itemList = []
        self.createItems()

        self.owner = Characters.NPC()
        self.owner.create("John Whickman", "human", "man", 57)

    def menu(self):
        self.Game.clearWindow()

        print "Hello {}. I'm {}. Here are my items:".format(self.Game.player.name, self.owner.name)
        print "You have {} golds.".format(self.Game.player.gold)

        for index, item in enumerate(self.itemList):
            print index, item

        backMenu = index + 1
        print backMenu, "Back to Main Menu"

        userInput = raw_input()

        if userInput == str(backMenu):
            self.Game.menu()

        self.shopping(int(userInput))

    def shopping(self, userItem):

        item = self.itemList[userItem]
        if self.owner.checkItem(self.Game.player, item):
            print "Well done! Here is your {}".format(item.name)
            self.Game.player.buy(item)

            self.Game.player.getInventory()

            time.sleep(3)
            self.Game.menu()
        else:
            self.Game.clearWindow()
            print "You don't have money for that {}.".format(item.name)
            time.sleep(5)
            self.menu()


    def createItems(self):
        item1 = Assets.Item()
        item1.create("Axe", 10, 35, 10)

        item2 = Assets.Item()
        item2.create("Spear", 25, 56, 25)

        item3 = Assets.Item()
        item3.create("Hammer", 68, 90, 35)

        self.itemList.append(item1)
        self.itemList.append(item2)
        self.itemList.append(item3)