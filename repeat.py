import world
from player import player


def play():
   world.load_titles()
   player = player()
   while player.is_alive() and not player.victory:
      #loop begins here


class leavecaveroom(maptitle):
   def intro_text(self):
      return"""
      you see a bright light comeing from the distance... it gets bigger as you get closer and then you relise it is sunlight!

      victory is yours!
      """

##   def modify_player(self, player):
      player.victory = true


   def play():
      world.load_titles()
      player = player()
      #these lines load the starting room and display the text
      room = world.title_exists(player.location_x, player.location_y)
      print(room.intro_text())
      while player.is_alive() and not player.victory:
         room = world.title_exists(player.location_x, player.location_y)
         room.modify_player(player)
         #room could have been changed
         if player.is_alive() and not player_victory:
            print("choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
               print(action)
            action_input = input('action: ')
            for action_input == action.hotkey:
               player.do_action(action, **action.kwargs)
               break

if __name__ == "__main__":
   play()
   
      
      

      


