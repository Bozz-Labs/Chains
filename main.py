import controller_main
import keyboard_main

game_type = input('(keyboard, controller) Game type:')
if game_type == 'keyboard':
  keyboard_main.main()
elif game_type == 'controller':
  controller_main.main()



