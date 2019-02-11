class Characters():
    def __init__(self):
        self.name = None
        self.gender = None

    def attack(self):
        print "ATTACK"


class Player(Characters):
    def __init__(self):
        Characters.__init__(self)

player1 = Player()
player1.attack()