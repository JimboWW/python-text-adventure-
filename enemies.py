#page( text_display )    Version 1.10    10-3-21
#name, hp, damage
class Enemy:
    def __init__(self): raise NotImplementedError("Don't create Enemy objects.")
    def __str__(self): return self.name
    def is_alive(self): return self.hp > 0

class HorseFly(Enemy):
    def __init__(self):
        self.name = "Horse fly"
        self.hp = 20
        self.damage = 2
class Rooster(Enemy):
    def __init__(self):
        self.name = "Rooster"
        self.hp = 30
        self.damage = 10
class BeeSwarm(Enemy):
    def __init__(self):
        self.name = "Swarm of Bees"
        self.hp = 100
        self.damage = 4
class MeanDog(Enemy):
    def __init__(self):
        self.name = "MeanDog"
        self.hp = 80
        self.damage = 15     
