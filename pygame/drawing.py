import pygame as py
from time import sleep
import math
py.init()

def drawRegularPolygon(surface, color, numSides, tiltAngle, x, y, radius):
  pts = []
  for i in range(numSides):
    x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / numSides)
    y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / numSides)
    pts.append([int(x), int(y)])
  py.draw.polygon(surface, color, pts)

width,height = 400,400
screen = py.display.set_mode((width,height))
rectColor = 10,120,120
circleColor = 250,0,100
lineColor = 236,245,66
eclipseColor = 200,200,34

py.draw.ellipse(screen,eclipseColor,py.Rect(30,30,100,150),0)
py.draw.arc(screen,(250,250,250),py.Rect(10,300,50,300),2,6.4,5)
py.draw.polygon(screen,(100,134,67),[(200,200),(250,250),(200,250),(150,200)])
py.draw.polygon(screen,(100,10,89),[(300,200),(250,250),(200,250),(250,200)])
py.draw.rect(screen,rectColor,py.Rect(30,30,60,60))
py.draw.circle(screen,circleColor,(200,200),20)
py.draw.line(screen,lineColor,(300,10),(300,300),10)
drawRegularPolygon(screen, (255, 180, 45), 5, 0, 100, 300, 50)
drawRegularPolygon(screen,(90,100,234),8,0,100,200,30)
py.draw.polygon(screen,(1,10,100),[(200,350),(200,300),(400,350)],5)
py.draw.ellipse(screen,(255,255,255),py.Rect(150,30,100,50),0)
py.draw.ellipse(screen,(255,255,255),py.Rect(100,50,100,50),0)
py.draw.ellipse(screen,(255,255,255),py.Rect(200,50,100,50),0)
py.draw.ellipse(screen,(255,255,255),py.Rect(150,55,100,50),0)
py.draw.polygon(screen,(89,67,90),[(300,300),(250,300),(225,300-(25*math.sqrt(3))),(250,300)-(50*math.sqrt(3)),(300,300)-(50*math.sqrt(3)),(325,300)-(25*math.sqrt(3))])

while True:
    py.display.flip()
    sleep(10/1000)