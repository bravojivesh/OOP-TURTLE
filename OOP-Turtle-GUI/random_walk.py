import turtle as tu
#https://docs.python.org/3/library/turtle.html turle graphics doc
import random

tu.colormode(255)

tim=tu.Turtle()
tim.width(7)
tim.speed("fast")
screen= tu.Screen()

angle_list= [90,180,270]
color_list=["red","green","blue","orchid","chocolate","coral"]

for _ in range(30):
    # tim.color(random.choice(color_list))
    a= random.randint(0,255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    tim.pencolor(a,c,b)
    tim.forward(40)
    tim.setheading(random.choice(angle_list))

screen.exitonclick()