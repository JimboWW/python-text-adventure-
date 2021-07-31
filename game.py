
import random

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is a very boring part of the cave.
        """
#selects and prints intro_text of MapTiles in play() loop - how?
class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        Victory is yours!
        """
class EnemyTile(MapTile):
		def __init__( self, x, y, enemies ):
			r = random.random()
			if r < 0.50:
				self.enemy = enemies.GiantSpider()
			elif r < 0.80:
					self.enemy = enemies.Ogre()
			elif r < 0.95:
					self.enemy = enemies.BatColony()
			else:
					self.enemy = enemies.RockMonster()
					
			super().__init__( x, y )

def tile_at( x, y ):
	if x < 0 or y < 0:
		return None
							
world_map = [
[ None, VictoryTile( 1, 0 ), None ],
[ None, EnemyTile( 1, 1, 1 ), None ],
[ EnemyTile( 0, 2, 1 ),StartTile( 1, 2 ),EnemyTile( 2, 2, 1 ) ],
[ None,EnemyTile( 1, 3, 1 ), None ]
