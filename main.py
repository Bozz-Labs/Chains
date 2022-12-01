import turtle
from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def home():
    print(request.headers)
    return render_template(
        'index.html',
        user_id=request.headers['X-Replit-User-Id'],
        user_name=request.headers['X-Replit-User-Name'],
        user_roles=request.headers['X-Replit-User-Roles']
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
def main():

    wn = turtle.Screen()
    wn.title('Chains')
    wn.bgcolor('black')
    wn.setup(width=800, height=800)
    wn.tracer(0)

    text = turtle.Turtle()
    text.speed(0)
    text.shape('square')
    text.color('white')
    text.penup()
    text.hideturtle()
    text.goto(0, 260)
    text.write('Chains', align='center', font=('Courier', 24, 'normal'))

    # Player
    player = turtle.Turtle()
    player.speed(0)
    player.shape('square')
    player.color('white')
    player.penup()
    player.goto(0, 0)

    # Function
    def player_up():
        y = player.ycor()
        y += 20
        player.sety(y)

    def player_down():
        y = player.ycor()
        y -= 20
        player.sety(y)

    def player_left():
        x = player.xcor()
        x -= 20
        player.setx(x)

    def player_right():
        x = player.xcor()
        x += 20
        player.setx(x)

    wn.listen()
    wn.onkeypress(player_up, 'w')
    wn.onkeypress(player_left, 'a')
    wn.onkeypress(player_down, 's')
    wn.onkeypress(player_right, 'd')
    wn.onkeypress(wn.bye, 'q')

    while True:
        wn.update()


main()
