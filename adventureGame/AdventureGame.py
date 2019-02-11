from gameModules import Assets, Characters, Places
import os, time

TESTING = True

class Game():
    def __init__(self):
        self.clearWindow()

        self.arena = Places.Arena(self)
        self.shop = Places.Shop(self)

        self.intro()

    def intro(self):
        print "-"*50, "BATTLE OF CLASSES", "-"*50
        print "This is your first time here. Who are you?"

        self.createPlayer()
        time.sleep(2)

        self.menu()

    def menu(self):
        self.clearWindow()

        print "Hello {}. What do you want to do?".format(self.player.name)

        print """
        1. Shop
        2. Arena
        3. Exit Game     
        """

        userInput = raw_input()
        if userInput == "3":
            print "Maybe next time..."
            exit()

        if userInput == "1":
            self.shop.menu()

        if userInput == "2":
            self.arena.menu()

    def createPlayer(self):
        if not TESTING:
            name = raw_input("Name?")
            characterClass = raw_input("What is your type?")
            gender = raw_input("What is your gender?")
            age = raw_input("How old are you?")
        else:
            name = "Laci"
            characterClass = "human"
            gender = "man"
            age = 29

        self.player = Characters.Player()

        # name, characterClass, gender, age
        self.player.create(name, characterClass, gender, age)

    def clearWindow(self):
        os.system("cls")


game = Game()