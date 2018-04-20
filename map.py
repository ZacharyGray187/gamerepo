import items, enemies

class maptitle:
   def __init__(self, x, y):
      self.x = x
      self.y = y

def intro_text(self):
   raise notimplementederror()

def modify_player(self, player):
   raise notimplementederror()

class startingroom(maptitle):
   def inro_text(self):
      return """ You find yourself in a cave with a flickering torch on the wall. You can make out four paths, each equally as dark and foreboding. """


   def modify_player(self, player):
      #room had no action on player
      pass


class lootroom(maptitle):
   def __init__(self, x, y, item):
      self.item = item
      super().__init__(x, y)

   def add_loot(self, player):
      player.inventory.append(self.item)

   def modify_player(self, player):
      self.add_loot(player)


class enemyroom(maptitle):
   def __init__(self, x, y, enemy):
      self.enemy = enemy
      super().__init__(x, y)

   def modify_player(self, the_player):
      if self.enemy.is_alive():
         the_player.hp = the_player.hp - self.enemy.damage
         print("enemy does {} damage. you have {} hp remaining.".format(self.enemy.damage, the_player.hp))
         
class emptycavepath(maptitle):
   def intro_text(self):
      return """ Another unremarkable part of the cave. You must venture onwards. """

   def modify_player(self, player):
      #room has no action on player
      pass

class giantspiderroom(enemyroom):
   def  __init__(self, x, y):
      super().__init__(x, y, enemies.giantspider())

   def intro_text(self):
      if self.enemy.is_alive():
         return """ A giant spider jumps down from its web right in front of you! """
      else:
         return """ the corpse of a dead spider rots on the ground. """

class finddaggerroom(lootroom):
   def __init__(self, x, y):
      super().__init__(x, y, items.dagger())

   def intro_text(self):
      return """ You notice something a little shiny in the corner. It's a dagger! You pick it up to fight back against the enemies. """

_world = {}
starting_position = (0, 0)

def load_titles():
   """prases a file that describes the world space into the _world object"""
   with open('resources/map.txt', 'r') as f:
      rows = f.readlines()
   x_max = len(rows[0].split('\t')) #assumes all rows will conatain the same number of tabs
   for y in range(len(rows)):
      cols = rows[y]/split('\t')
      for x in range(x_max):
         title_name = cols[x].replace('\n', '') #windows users may need to replacem'\r\n'
         if title_name == 'startingroom':
            global starting_position
            starting_position = (x, y)
         _world[(x, y)] = none if title_name == '' else getattr(__import__('titles'), title_name)(x, y)


   def title_exists(x, y):
      return _world.get((x, y))
      
      



