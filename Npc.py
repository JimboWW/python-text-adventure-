#page( world )    Version 1.09     9-25-21
import Items

#name, gold, inventory
class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")
    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self ):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [ Items.Bread(), Items.Rock() ]
                      
"""class Magic(Trader):
    def __init__(self ):
        self.name = "Magic"
        self.gold = 100
        self.inventory = [
            items.HealingPotion(), items.HealingPotion(), items.HealingPotion(),
            items.Poison(), items.Poison(), items.Poison() ]
         
class Armor(Trader):
    def __init__(self ):
        self.name = "Armor"
        self.gold = 100
        self.inventory = [  items.LeatherArmor() ]
         
class Weapon(Trader):
    def __init__(self ):
        self.name = "Weapon"
        self.gold = 100
        self.inventory = [
            items.Rock(), items.Dagger(), items.RustySword() ]"""
