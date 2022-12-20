import controller_main
import keyboard_main
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("resources/Menu.gif")
wn.setup(width=579, height=311)
wn.title("Chains")

def controller(x, y):
  controller_main.main()
  wn.bye()

def keyboard(x, y):
  keyboard_main.main()
  wn.bye()

wn.onclick(controller, btn=3, add=None)

wn.onclick(keyboard, btn=1, add=None)

