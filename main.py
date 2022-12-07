import turtle
import time

def main():
  #Variables  
  wn = turtle.Screen()
  wn.title('Chains')
  wn.bgcolor('black')
  wn.setup(width=579, height=311)
  wn.tracer(0)
  wn.addshape('resources/Flashlight.gif')
  wn.addshape('resources/Toolbar.gif')
  wn.addshape('resources/Player.gif')
  wn.addshape('resources/Player Up.gif')
  wn.addshape('resources/Player Down.gif')
  wn.addshape('resources/Player Right.gif')
  wn.addshape('resources/Player Left.gif')
  wn.addshape('resources/Sneak.gif')
  wn.addshape('resources/Medkit.gif')
  wn.addshape('resources/Chains Logo.gif')
  
  text = turtle.Turtle()
  text.speed(0)
  text.shape('square')
  text.color('white')
  text.penup()
  text.hideturtle()
  text.goto(0, 260)
  text.write('Chains: Tutorial', align='center', font=('Courier', 24, 'normal'))

  instructions = turtle.Turtle()
  instructions.speed(0)
  instructions.shape('square')
  instructions.color('white')
  instructions.penup()
  instructions.hideturtle()
  instructions.goto(0, 220)
  instructions.write('Instructions', align='center', font=('Courier', 24, 'normal'))

  coords = turtle.Turtle()
  coords.speed(0)
  coords.shape('square')
  coords.color('white')
  coords.penup()
  coords.hideturtle()
  coords.goto(0, -220)
  coords.write('x: 0, y: 0', align='center', font=('Courier', 24, 'normal'))

  # Sneak
  sneak = turtle.Turtle()
  sneak.shape('resources/Sneak.gif')
  sneak.speed(0)
  sneak.penup()
  sneak.hideturtle()
  
  # Player
  player = turtle.Turtle()
  player.speed(0)
  player.shape('resources/Player.gif')
  player.penup()
  player.goto(0, 0)

  # toolbar
  toolbar = turtle.Turtle()
  toolbar.speed(0)
  toolbar.shape('resources/Toolbar.gif')
  toolbar.penup()
  toolbar.goto(-240, 130)
  
  medkit = turtle.Turtle()
  medkit.shape('resources/Medkit.gif')
  medkit.speed(0)
  medkit.goto(0, 0)
  medkit.penup()
  medkit.hideturtle()

  room_num = 0
  
  items = [
    
  ]

  light_level = 10

  room_change = [False]

  health_level = [10]
  
  display_health = turtle.Turtle()
  display_health.speed(0)
  display_health.shape('square')
  display_health.color('white')
  display_health.penup()
  display_health.hideturtle()
  display_health.goto(0, -260)
  display_health.write('{}'.format(health_level[0]), align='center', font=('Courier', 24, 'normal'))

  # Functions
  def player_up():
    y = player.ycor()
    y += 40
    player.sety(y)
    player.shape('resources/Player Up.gif')

  def player_down():
    y = player.ycor()
    y -= 40
    player.sety(y)
    player.shape('resources/Player Down.gif')

  def player_left():
    x = player.xcor()
    x -= 40
    player.setx(x)
    player.shape('resources/Player Left.gif')

  def player_right():
    x = player.xcor()
    x += 40
    player.setx(x)
    player.shape('resources/Player Right.gif')

  def move_forward():
    player.goto(0, -80)
    time.sleep(0.5)
    wn.bgpic('resources/Transition.gif')
    time.sleep(0.5)
    sneak.hideturtle()

  def move_backward():
    player.goto(0, 80)
    time.sleep(0.5)
    wn.bgpic('resources/Transition.gif')
    time.sleep(0.5)
    sneak.hideturtle()

  def heal(x, y):
    if health_level[0] < 9:
      health_level[0] += 2
      medkit.hideturtle()

  def suicide():
    health_level[0] -= 1

  def damage(amount):
    health_level[0] -= amount

  wn.listen()
  wn.onkeypress(player_up, 'w')
  wn.onkeypress(player_left, 'a')
  wn.onkeypress(player_down, 's')
  wn.onkeypress(player_right, 'd')
  wn.onkeypress(wn.bye, 'q')
  wn.onkeypress(suicide, 'k')
  medkit.onclick(heal, btn=1, add=None)

  while True:
    wn.update()

    display_health.clear()
    display_health.write('Health: {}'.format(health_level), align='center', font=('Courier', 24, 'normal'))
    
    if room_num == 0:
      wn.bgpic('resources/Tutorial Room 0.gif')
      
    if room_num == 1:
      wn.bgpic('resources/Tutorial Room 1.gif')
      medkit.showturtle()
      if medkit.distance(player) == 0:
        medkit.goto(-230, 130)
        items.append('medkit')

    if room_num == 2:
      if room_change[0] == False:
        wn.bgpic('resources/Tutorial Room 2.gif')
      instructions.clear()
      instructions.write('You can open drawers in this game by clicking anywhere on the screen. Try it!', align='center', font=('Courier', 24, 'normal'))
      
      def flashlight(x, y):
        if room_num == 2:
          room_change.pop(0)
          room_change.append(True)
          items.append('flashlight')
          wn.bgpic('resources/Tutorial Room 2 - Open Drawer.gif')
          instructions.clear()
          instructions.write('You picked up: Flashlight', align='center', font=('Courier', 24, 'normal'))
      if room_num == 2:
        wn.onclick(flashlight, btn=2, add=None)

    if room_num == 3:
      
      light_level -= 6
      
      if player.ycor() == 80:       
        wn.bgpic('resources/Jumpsare 1.gif')
        sneak.hideturtle()
      elif player.xcor()== -80 and player.ycor() == -120:
        wn.bgpic('resources/Sneak Fullscreen.gif')
        sneak.hideturtle()
      else:  
        wn.bgpic('resources/Tutorial Room 3.gif')

      sneak.goto(-80, -90)

      sneak.showturtle()
    if player.xcor() < -240:
      player.goto(-240, player.ycor())
      
    if player.xcor() > 240:
      player.goto(240, player.ycor())
      
    if player.ycor() > 120:
      player.goto(player.xcor(), 120)
      
    if player.ycor() < -120:
      player.goto(player.xcor(), -120)
      
    if player.ycor() == 120 and player.xcor() == 0:
      room_num += 1
      move_forward()
      room_change.pop(0)
      room_change.append(False)
      medkit.hideturtle()
      
    if player.ycor() == -120 and player.xcor() == 0 and room_num > 0:
      room_num -= 1
      move_backward()
      room_change.pop(0)
      room_change.append(False)
      medkit.hideturtle()

    coords.clear()
    coords.write('x: {}, y: {}'.format(player.xcor(), player.ycor()), align='center', font=('Courier', 24, 'normal'))

    if 'medkit' in items:
      medkit.showturtle()

    if 'flashlight' in items:
      flashlight = turtle.Turtle()
      flashlight.shape('resources/Flashlight.gif')
      flashlight.penup()
      flashlight.speed(0)
      flashlight.goto(-256, 130)
      flashlight.on = False
      
      def flash_on(x, y):
        if light_level < 5 and flashlight.on == False:
          player.color('white')
          flashlight.on = True
        else:
          instructions.clear()
          instructions.write("Cannot use flashlight tight now.", align='center', font=('Courier', 24, 'normal'))

      def flash_off(x, y):
        if flashlight.on == True:
          player.color('white')
          flashlight.on = False
        else:
          instructions.clear()
          instructions.write("It's too bright in here", align='center', font=('Courier', 24, 'normal'))

      flashlight.onclick(flash_on, btn=1, add=None)
main()

