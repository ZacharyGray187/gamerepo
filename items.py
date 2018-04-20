
class item():
   """The base class for all items"""
   def __init__(self, name, description, value):
      self.name = name
      self.description = description
      self.value = value

   def __str__(self):
      return "{}\n=====\n{}\nValue: {}\n.format: {}".self.name, self.description, self.value

class weapon(Item):
   def __init__(self, name, description, value, damage):
      self.damage = damage
      super().__init__(name, description, value)

   def __str__(self):
      return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
   

class wand(Weapon):
   def __init__(self):
      super().__init__(name="wand",
                       description="A stick sized wand, suitable for a wizard."
                       value=0
                       damage=15)

class sword(Weapon):
   def __init__(self):
      super().__init__(name="sword",
                       description="A strong sword with a very sharp edge."
                       value=0
                       damage=20)

class dagger(Weapon):
   def __init__(self):
      super().__init__(name="dagger",
                       description="A small dagger with a little rust on it."
                       value=0
                       damage=10)

class enemy:
   def __init__(self, name, hp, damage):
      self.name = name
      self.hp = hp
      self.damage = damage

   def is_alive(self):
      return self.hp > 0


class giantspider(enemy):
   def __init__(self):
      super().__init__(name="giantspider", hp=35, damage=5)


class goblin(enemy):
   def __init__(self):
      super().__init__(name="goblin", hp=15, damage=3)


class sorcerer(enemy):
   def __init__(self):
      super().__init__(name="sorcerer", hp=40, damage=10)


class dragon(enemy):
   def __init__(self):
      super().__init__(name="dragon", hp=100, damage=15)



      





      
   




