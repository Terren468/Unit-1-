import turtle
from turtle import *
t = Turtle()

t.shape('turtle') 
def square(x,y):
    for i in range(4):
        t.forward(100)
        t.left(90)
square(100, 90)


def square_thing(x,y):
    for i in range(60):
        square(x,y)
        t.right (5)
square_thing (100,90)

