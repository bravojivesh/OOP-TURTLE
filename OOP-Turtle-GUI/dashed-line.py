import turtle as tu

timmy=tu.Turtle()



# for _ in range (4):
#     timmy.forward(10)
#     # timmy.right(90)
# for steps in range(50):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(10)

#JH:WAY1: THE FOLLOWING BLOCK WORKS--USING COLORS.
# steps= 10
# for _ in range(15):
#         timmy.color("black")
#         timmy.forward(steps)
#         timmy.color("white")
#         # timmy.forward(steps+50)
#         # timmy.home()
#         timmy.forward(steps)

#JH: WAY2: Using penup and pendown
for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()




screen=tu.Screen()
screen.exitonclick()
