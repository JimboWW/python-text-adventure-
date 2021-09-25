#page( Items )    Version 1.09     9-25-21

class items:
    def __init__(self, name_): self.name = name
    def __str__(self): return self.name
    
#inventory
class Rock(items):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 100 #1 - 100 for testing
        self.value = 1

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)
        
class Bread( Consumable ):
    def __init__(self):
        self.name = "Bread"
        self.healing_value = 10
        self.value = 12
