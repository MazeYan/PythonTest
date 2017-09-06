# e2.2DrawPython.py

# from turtle import *
from turtle import setup, penup, fd, pendown
from turtle import pensize, pencolor,seth,circle
  
setup(650, 300, 200, 200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("violet")
seth(-40)
for i in range(4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/2)
fd(40)
circle(16, 180)
fd(40 * 2/3)
