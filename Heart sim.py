import math
from turtle import *

def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return (13 * math.cos(t)- 5*\
    math.cos(2 * t)- 2 *\
    math.cos(3 * t)- \
    math.cos(4 * t))

speed(900000)
bgcolor("white")
for i in range(6000):
    goto(heart_x(i) *20 , heart_y(i) *20)
    for j in range(1):
        color("pink")
    goto(0, 0)
done()
