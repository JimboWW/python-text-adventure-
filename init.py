#page( init )    Version 1.09     9-25-21
import Items, world

class Player:
    def __init__( self ):
        self.name = "Player"
        self.x = world.start_tile_location[ 0 ]
        self.y = world.start_tile_location[ 1 ]
        self.hp = 100
        self.level = 1
        self.experience = 100
        self.inventory = [ Items.Bread(), Items.Rock() ]
        self.pclass = str("janitor")
        self.gold = 100
        self.hp = 100

    def hud(self):
        print( "Health:", self.hp, "Level:", self.level,\
        "Experience:", self.experience, "Class:", self.pclass ,"Gold:", self.gold , "\n" )   

    def print_inventory(self):
        print("\nInventory:")
        for items in self. inventory:
            print( '*', items )
        print( "Gold: {}".format(self.gold))
        input('\nPress return when finished viewing inventory')   

    def move(self, dx, dy): self.x += dx; self.y += dy
    def move_north(self): self.move(dx=0, dy=-1)
    def move_south(self): self.move(dx=0, dy=1)
    def move_east(self): self.move(dx=1, dy=0)
    def move_west(self): self.move(dx=-1, dy=0)    
            
    def is_alive(self):
        return self.hp > 0
          
    def attack(self):
        room = world.tile_at( self.x, self.y )
        enemy = room.enemy
        print("You use {} against {}!".format( Items.Rock, enemy.name ) )
        enemy.hp = enemy.hp - Items.Rock().damage
        self.hp = self.hp - enemy.damage
        print("Enemy does {} damage. You have {} HP remaining.".\
        format(enemy.damage, self.hp))       
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))
        input( 'Press return when finished' )
        
    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
            
#9-25-21 To Do:
    #X1. Add a functional enemy
        #X1a. after enemy dead, make move functions available
    #X2. Add a functional trader
    #X3. Print inventory items on separate lines like this: * Bread
    #X4. Add enemy damage to player
    #X5. Fix error in trade: Cannot quit tile
    #X6. Error check in trade if user types out of index range number - invalid
    #X7. Add gold to hud()

""" #class template
class Temp:
    def __init__(self): pass
    def __str__(self): return self.name    
    def temp_func(self):return self """
