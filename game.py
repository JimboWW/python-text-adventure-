from player import Player
import world


II 
 
def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            player.move_north()
        elif action_input in ['s', 'S']:
            player.move_south()
        elif action_input in ['e', 'E']:
            player.move_east()
        elif action_input in ['w', 'W']:
            player.move_west()
        elif action_input in ['i', 'I']:
            player.print_inventory()
        else:
            print("Invalid action!")

def get_player_command():
    return input('Action: ')

play()
#'room.intro_text()' is calling and prints 'maptile' text. Each 'maptile' has an 
#'intro_text' function. When called, it displays its text - a room description.

#'room' is 'world' modules 'tile_at', sets x,y to var 'player' x,y, an instantiation 
#of 'player' modules 'Player()' class.Player()' x,y vars are also used by internal 
#'move' functions to simulate player movement, selecting a 'room' that prints to 
#screen, a description of the 'player' location.

#The 'world' module 'mapTile' function 'introText' uses 'return' to print 
#room descriptions.'tile_at'select objects in the 'world_map' list of lists, 
#those objects having set x,y values. 

#'room' is world module tile_at() function that prints room descriptions of
#the 'tile_at' location, so when it finds the room in the 'world_map' 
#list of lists that matches its x,y values, it prints that rooms description.

#Still, the above explaination doesn't fully explain how the room description 
#text got printed, so now I'm approaching the explanation from a different 
#perspective.
#Embeddd in the player modules Player() class, is a function called '
#print_inventory()' and another called 'most_powerful_weapon()' and both 
#relate to printing inventory item names and how those names are printed. 
#Very similar problem to printing  dungeon room descriptions, a description 
#for a weapon or room needs to be selected then printed to screen.
#In both cases, a list is used as a container for objects: weapons/rooms.
