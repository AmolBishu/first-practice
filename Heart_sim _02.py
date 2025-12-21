import math
from turtle import Screen, Turtle, done

def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return (13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t))
screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")

pen = Turtle()
pen.hideturtle()
pen.speed(0)      
pen.pensize(2)
pen.color("white")
pen.penup()

scale = 20        
steps = 720       
for i in range(steps + 1):
    t = (i / steps) * 2 * math.pi   
    x = heart_x(t) * scale
    y = heart_y(t) * scale
    pen.goto(x, y)
    pen.pendown()

done()
