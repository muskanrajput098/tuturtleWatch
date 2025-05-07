import turtle
from datetime import datetime

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title(" Muskan Rajput")
screen.setup(width=700, height=700)

# Clock face
dial = turtle.Turtle()
dial.hideturtle()
dial.pensize(6)
dial.color("gold")
dial.penup()
dial.goto(0, -300)
dial.pendown()
dial.circle(300)

# Hour marks
dial.penup()
dial.goto(0, 0)
dial.color("white")
for hour in range(12):
    dial.forward(250)
    dial.pendown()
    dial.forward(20)
    dial.penup()
    dial.goto(0, 0)
    dial.right(30)

# Boutique name
dial.goto(0, -270)
dial.color("hotpink")
dial.write("Boutique by Muskan Rajput", align="center", font=("Courier", 18, "bold"))

# Create hands
def create_hand(length, color, width):
    hand = turtle.Turtle()
    hand.shape("arrow")
    hand.color(color)
    hand.shapesize(stretch_wid=width, stretch_len=length)
    hand.speed(0)
    hand.penup()
    return hand

second_hand = create_hand(1.2, "red", 0.4)
minute_hand = create_hand(1.0, "white", 0.6)
hour_hand = create_hand(0.8, "gold", 0.8)

# Update function
def update_clock():
    now = datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour % 12

    second_hand.setheading(90 - sec * 6)
    minute_hand.setheading(90 - minute * 6)
    hour_hand.setheading(90 - (hour * 30 + minute * 0.5))

    screen.ontimer(update_clock, 1000)

update_clock()
turtle.done()
