class People:
    def __init__(self):
        raise NotImplementedError("Do not create raw People objects.")
    def __str__(self): return self.name
    def is_alive(self): return self.hp > 0

class TownDrunk(People):
    def __init__(self):
        self.name = "Town Drunk"
        self.hp = 20
        self.damage = 2
class Rogue(People):
    def __init__(self):
        self.name = "Rogue"
        self.hp = 4
        self.damage = 3
class BattleScarredVeteran(People):
    def __init__(self):
        self.name = "Battle Scarred Veteran"
        self.hp = 10
        self.damage = 3()
class Beggar(People):
    def __init__(self):
        self.name = "Beggar"
        self.hp = 8
        self.damage = 2
