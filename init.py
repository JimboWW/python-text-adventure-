#page( init )    Version 1.10     10-3-21
import Items, world

class Player:
    def __init__( self ):
        self.name = "Player"
        self.x = world.start_tile_location[ 0 ]
        self.y = world.start_tile_location[ 1 ]
        self.hp = 100
        self.level = 1
        self.experience = 100
        self.pclass = "Janitor"
        self.gold = 100
        self.inventory = [ Items.Bread(), Items.Rock() ]
    def hud(self):
        print( "Health:", self.hp, "Level:", self.level,\
        "Experience:", self.experience, "Class:", self.pclass ,"Gold:", self.gold , "\n" ) 
    def print_inventory(self):
        print("\nInventory:")
        for x in range( len( self.inventory ) ) :
            print( "*", self.inventory[ x ] )
        #for i in self.inventory : print( "*", i ) #old version
        print( "Gold: {}".format(self.gold))
        input('\nPress return when finished viewing inventory')   
    def pie(self):
        valid = False
        while not valid:
            choice = input("eat pie?")
            if choice in [ "y", "Y" ]:
                self.hp = 100
                print("You feel much better!")
                print("Health:", self.hp)
                valid = True
    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, Items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return
        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))
        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon
    def move(self, dx, dy): self.x += dx; self.y += dy
    def move_north(self): self.move(dx=0, dy=-1)
    def move_south(self): self.move(dx=0, dy=1)
    def move_east(self): self.move(dx=1, dy=0)
    def move_west(self): self.move(dx=-1, dy=0)                
    def is_alive(self): return self.hp > 0          
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
            self.experience += 20
            self.level += int( self.experience / 500 )
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))
        input( 'Press return when finished' )        
    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
          
#9-26-21 To Do:
    #X1. Add a save function for user to choose
    #X2. Add a load function for user to choose
    #X3. Change rooms and tile text to make this small world a small story
        #3a. Story: You are a young boy in an isolated, 15th century village.
                 #your Dad was an adventurer and that is what you want to do
                 #for centuries now, the village has dug and placed it's dead
                 #underground. Adventuring means to go down into this multiple
                 #leveled catacombs and battle the creatures inside before they get
                 #out and into the town. Your Dad died fighting for the village. Your
                 #Mom is against your plans. The crypts entrance is guarded and
                 #only trained, certified adventurers may enter. The village itself,
                 #is small but has its own dangers. There is a constable, a trainer,
                 #a stables(to work in). There are 4 stores, magic, armor, general
                 #goods, weapons.
    #X4. Add functional player attributes that work, experience, leveling, etc.
    #X5. Add a Victory tile, and to dsl
    #X6. Refactor code again... I've eliminated 2 pages
    #X7. Fix again, inventory display, save, load...
#10-3-21 ToDo:
    #1. Don't seem to have easy way to add rooms, characters, enemies, items
           #I would like to have that. Rooms add in world, enemies in enemies
           #items in Items, characters in Npc. Would be nice to have one page 
           #to enter all and each page like world, Items, enemies, Npc would feed
           #from that page.
    #2. Classes are like cookie cutters. Think I should make better use of
           #objects instantiated from classes
    #X3. Get rid of duplicate trader RoomTile functions in world
    #4. Do a complete walkthrough this small world with no errors
    #5. Get the Apple pie thing working
    
""" #class template
class Temp:
    def __init__(self): pass
    def __str__(self): return self.name    
    def temp_func(self):return self """
    
#ARRANGEMENT:
"""items - weapons,  
    rooms, 
    world map list, 
    tile_at() function, 
    Player class, 
    get_player_command() function, 
    play() function and loop
    
    pages: 
        items: (consumables, armor, gold, weapons) >>>
        world: (enemies, trade) >>>
            world map list[ ], tile_at() >>>
        init: Player class >>>
        main: get_player_command(), play() loop>"""
        
        #Items > world  >
            #enemies, rooms, trader, trade, swap, other traders, 
            #world dsl(map), is_dsl_valid, tile_type_dict, world_map[]
            #start_tile_location, tile_at
        #from init: Player > 
        #from text_display: IntroScreen 
        #main >
             #save, load, action_adder
             #get_available_actions, choose_action
             #IntroScreen.intro_text()
             #world.parse_world_dsl()
             #player = Player()
             #game loop
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
