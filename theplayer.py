import items

class player():
   def __init__(self):
      self.inventory = [items.gold(15), items.dagger()]
      self.hp = 100
      self.location_x, self.location_y = world.starting_position
      self.victory = false

   def is_alive(self):
      return self.hp > 0

   def print_inventory(self):
      for item in self.inventory:
         print(item, '\n')

   def move(self, dx, dy):
      self.location_x += dx
      self.location_y += dy
      print(world.title_exists(self,location_x, self.location_y).intro_text())

   def move_north(self):
      self.move(dx=0, dy=-1)

   def move_south(self):
      self.move(dx=0, dy=1)

   def move_west(self):
      self.move(dx=-1, dy=0)

   def move_east(self):
      self.move(dx=1, dy=0)

   def attack(self, enemy):
      best_weapon = none
      max_dmg = 0
      for i in self.inventory:
         if isinstance(i, items.weapon):
            if i.damage > max_dmg:
               max_dmg = i.damage
               best_weapon = i

      print("You use {} against {}!".format(best_weapon.name, enemy.name))
      enemy.hp -= best_weapon.damage
      if not enemy.is_alive():
         print("You killed {}!.format(enemy.name)")
      else:
            print("{} hp is {}.format(enemy.name, enemy.hp)")


import player

class action():
   def __init__(self, method, name, hotkey, **kwargs):
       self.method = method
       self.hotkey = hotkey
       self.name = name
       self.kwargs = kwargs

   def __str__(self):
       return "{}: {}".format(self.hotkey, self.name)


class movenorth(action):
   def __init__(self):
      super().__init__(method=player.move_north, name='move north', hotkey='w')

class movesouth(action):
   def __init__(self):
      super().__init__(method=player.move_south, name='move south', hotkey='s')
               
class moveeast(action):
   def __init__(self):
      super().__init__(method=player.move_east, name='move east', hotkey='d')

class movewest(action):
   def __init__(self):
      super().__init__(method=player.move_west, name='move west', hotkey='a')

class viewinventory(action):
   """prints the player's inventory"""
   def __init__(self):
      super().__init__(method=player.print_inventory, name='view inventory', hotkey='i')

class attack(action):
   def __init__(self, enemy):
      super().__init__(method=player.attack, name='attack', hotkey='l', enemy=enemy)


import items, enemies, actions, world
def adjacent_moves(self):
   """returns all move action for adjacent titles."""
   moves = []
   if world.title_exists(self.x + 1, self.y):
      moves.append(actions.moveeast())
   if world.title_exists(self.x - 1, self.y):
      moves.append(actions.movewest())
   if world.title_exists(self.x, self.y - 1):
      moves.append(actions.movenorth())
   if world.title_exists(self.x, self.y + 1):
      move.append(actions.movesouth())

def available_actions(self):
   """returns all of the available actions in this room."""
   moves = self.adjacent_moves()
   moves.append(actions.viewinventory())

   return moves

   def do_action(self, action, **kwargs):
      action_method = gettr(self, action.method.__name__)
      if action_method:
         action_method(**kwargs)


import random #note the new import!
import items, world

class player:
   #existing code omitted for brevity

   def flee(self, title):
      """moves the player randomly to an adjscent title"""
      available_moves = title.adjacent_moves()
      r = random.randint(0, len(available_moves) - 1)
      self.do_action(available_moves[r])


class flee(action):
   def __init__(self, title):
      super().__init__(method=player.flee, name="flee", hotkey='f', title=title)


class enemyroom(maptitle):
   def __init__(self, x, y, enemy):
      self.enemy = enemy
      super().__init__(x, y)

   def modify_player(self, the_player):
      if self.enemy.is_alive():
         the_player.hp = the_player.hp - self.enemy.damage
         print("enemy does {} damage. you have {} hp remaining.".format(self.enemy.damage, the_player.hp))

   def available_actions(self):
      if self.enemy.is_alive():
         return [actions.flee(title=self), actions.attack(enemy=self.enemy)]

      else:
         return self.adjacent_moves()

      
      
      



      

   
      
      
   

      
         
                         
