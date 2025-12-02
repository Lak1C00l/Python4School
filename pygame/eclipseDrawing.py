import pygame as py
from time import sleep

width,height = 400,400
screen = py.display.set_mode((width,height))
eclipseColor = 200,200,34

py.draw.ellipse(screen,eclipseColor,py.Rect(30,30,100,150),0)
py.draw.arc(screen,(250,250,250),py.Rect(10,300,50,300),2,6.4,5)
py.draw.polygon(screen,(100,134,67),[(200,200),(250,250),(200,250),(150,200)])
py.draw.polygon(screen,(100,10,89),[(300,200),(250,250),(200,250),(250,200)])

while True:
    py.display.flip()
    sleep(10/1000)