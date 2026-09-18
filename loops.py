import turtle
from turtle import *
t = Turtle()
def add (x,y):
     return x+y 
t.shape('turtle') 
def square(x,y):
    for i in range(4):
        t.forward(100)
        t.left(90)
""" square(100,90)  """

""" def square_thing(x,y):
    for i in range(60):
        square(x,y)
        t.right (5)
square_thing (100,90) """ 

def add (x,y):
     return x+y 
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
def evil_square():
   y = 90
   c = 5
   for i in range (60):
        square(c,y) 
        c += 5
        t.left(-5)
evil_square() 

def not_square (x,y):
    for i in range(5): 
        t.forward(x) 
        t.left(y) 
not_square(100, 144)







