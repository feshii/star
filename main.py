import turtle
import random
t=turtle.Turtle()
w=turtle.Screen()
t.speed(0)
w.bgcolor("black")
t.color("white")
def star():
    for i in range(5):
        t.forward(10)
        t.right(144)
for i in range(100):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    t.penup()
    t.goto(x,y)
    t.pendown()
    star()
t.penup()
t.goto(0,170)
t.pendown()
t.begin_fill()
t.circle(70)
t.end_fill()
w.exitonclick()
