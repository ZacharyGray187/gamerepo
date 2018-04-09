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


