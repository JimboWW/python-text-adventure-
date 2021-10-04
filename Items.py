#page( Items )    Version 1.10     10-3-21
class items:
    def __init__(self):
        raise NotImplementedError("Do not create raw items objects.")
    def __str__(self):return "{}".format( self.name )
    def __repr__(self):return "{}".format( self.name )

class Rock(items):
    def __init__( self ):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 100 #1 - 100 for testing
        self.value = 1
        super( Rock ).__init__(  )        
class Dagger(items):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
                           "Somewhat more dangerous than a rock."
        self.damage = 8
        self.value = 20
        super( Dagger ).__init__(  )      
class RustySword(items):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age, " \
                           "but still has some fight in it."
        self.damage = 12
        self.value = 100
        super( RustySword ).__init__(  )
        
class Armor:
    def __init__( self ):
        raise NotImplementedError("Do not create raw Armor objects.")
    def __str__( self ):return self.name
class LeatherArmor( Armor ):
    def __init__(self):
        self.name = "Leather Armor"
        self.description = "Used leather armor but in reasonably good condition."
        self.value = 50
        self.protect = 15
        super( LeatherArmor ).__init__(  )
        
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")
    def __str__(self):return "{}".format( self.name )
    def __repr__(self):return "{}".format( self.name )
class Bread( Consumable ):
    def __init__( self ):
        self.name = "Bread"
        self.healing_value = 10
        self.value = 12
        super( Bread ).__init__(  )       
class Pie(Consumable):
    def __init__(self):
        self.name = "Mom's Apple Pie"
        self.healing_value = 50
        self.value = 0
        super( Pie ).__init__(  )        
class HealingPotion(Consumable):
    def __init__(self):
        self.name = "bgarfer"
        self.healing_value = 50
        self.value = 60
        super( HealingPotion ).__init__(  )        
class Poison(Consumable):
    def __init__(self):
        self.name = "wagjel"
        self.healing_value = -30
        self.value = 60
        super( Poison ).__init__(  )
