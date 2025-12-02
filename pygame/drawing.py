import pygame as py
from time import sleep
py.init()

width,height = 400,400
screen = py.display.set_mode((width,height))
rectColor = 10,120,120
circleColor = 250,0,100
lineColor = 236,245,66
#drwing rect
py.draw.rect(screen,rectColor,py.Rect(30,30,60,60))
py.draw.circle(screen,circleColor,(200,200),20)
py.draw.line(screen,lineColor,(300,10),(300,300),10)

while True:
    py.display.flip()
    sleep(10/1000)