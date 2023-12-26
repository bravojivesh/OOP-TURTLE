import turtle as tu
#https://docs.python.org/3/library/turtle.html turle graphics doc
import random

tim=tu.Turtle()
pen=tu.Turtle()
screen= tu.Screen()

color_list=["red","green","blue","orchid","chocolate","coral"]

#JH: WAY 1
# for x in range(3,10):
#     color_list=["red","green","blue","orchid","chocolate","coral"]
#     tim.color(random.choice(color_list))
#     for _ in range(x):
#         tim.forward(100)
#         tim.right(360/x)

#WAY 2: with functions
def create_shapes(sides):
    angle=360/sides
    color1= random.choice(color_list)
    for _ in range (sides):
        tim.color(color1)
        tim.forward(100)
        tim.left(angle)

for x in range (3,11):
    create_shapes(x)

screen.exitonclick()
