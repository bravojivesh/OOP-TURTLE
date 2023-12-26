import turtle as tu
#https://docs.python.org/3/library/turtle.html turle graphics doc
import random

tu.colormode(255)
def rand_color():
    list=[]
    for x in range (3):
        list.append(random.randint(0,255 ))
        #this will create a list like [11,234,30]
    return tuple(list) #this will convert the list into tuple so that tu.color can use the output as an input



tim=tu.Turtle()
tim.width(2)
tim.speed("fastest")
screen= tu.Screen()

x=40 #this will be the angle or gap between circle

for _ in range (int(360/x)): #decides many times should it move and make a circle.
    # 360 coz we want it to stop after making a full cycle.

    tim.color(rand_color())
    tim.circle(100)
    tim.setheading(tim.heading()+x) #this will set proper angle every time a cricle is drawn

    # tim.setheading(x)
    # x+=5 #by observation the places where the turtle starts is absolute. So I had to add values everytime.

rand_color()












screen.exitonclick()