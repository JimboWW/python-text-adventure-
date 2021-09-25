#page( world )    Version 1.09     9-25-21
import Npc

class Enemy:
    def __init__(self): raise NotImplementedError("Don't create raw Enemy obj.")
    def __str__(self):return self.name
    def is_alive(self):
        return self.hp > 0

class HorseFly(Enemy):
    def __init__(self ):
        self.name = "Horse fly"
        self.hp = 20
        self.damage = 2

class RoomTile:
    def __init__(self, x, y): self.x = x; self.y = y
    def intro_text(self):raise NotImplementedError("Create a subclass instead!")
    def modify_player(self, player): pass
    
class Start(RoomTile):
    def intro_text( self ): return """Start room\n"""
    
class CobbleRoad(RoomTile):
    def intro_text( self ): return """Cobblestone Road \n"""       

class EnemyTile( RoomTile ):
    def __init__( self, x, y ):
        self.x = x; self.y = y
        self.enemy = HorseFly()
        self.alive_text = "A horse fly tries to bite you!!"
        self.dead_text = "The horse fly is dead."
        super().__init__( x, y )
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

class TraderTile(RoomTile):
    def __init__(self, x, y):
        #if tile_type_dict.get("a") == True: self.trader =  Enpc.Armor()
        #if tile_type_dict.get("w") == True: self.trader =  Enpc.Weapon()
        #if tile_type_dict.get("t") == True: self.trader =  Npc.Trader()
        #if tile_type_dict.get("m") == True: self.trader =  Enpc.Magic()
        self.trader = Npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:            
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return input( "Press return to exit shop." )
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                print( self.trader.inventory )
                self.trade(buyer=player, seller= self.trader )
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return input( "Press return to continue shopping..." )
            else:
                try:
                    choice = int(user_input)
                    try:                      
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except IndexError:
                        print( "Invalid choice!" )
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def intro_text(self):
        return """
        An expectant middle age man tries not to look overly eager to trade.
        """

world_dsl = """
|x|x|x|x|x|x|x|
|x|c|c|c|c|c|x|
|x|c|x|e|x|c|x|
|x|c|c|h|c|c|x|
|x|c|x|t|x|c|x|
|x|c|c|c|c|c|x|
|x|x|x|x|x|x|x|"""

def is_dsl_valid(dsl):
    if dsl.count("|h|") != 1:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

tile_type_dict = {
                  "h": Start,
                  "c": CobbleRoad,
                  "e": EnemyTile,
                  "t": TraderTile,
                  "x": None }
                                            
world_map = []

start_tile_location =  None
def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == Start:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)
        world_map.append(row)

parse_world_dsl()

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
