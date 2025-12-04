import pygame as py
from time import sleep

length,width = 600,600
screen = py.display.set_mode((width,length))
pos = (0,0)
backround = (0,0,0)

while True:
    for event in py.event.get():
        if event.type == py.MOUSEMOTION:
            pos = py.mouse.get_pos()
    screen.fill(backround)
    py.draw.polygon(screen,(100,100,100),[
        (pos[0]+25,pos[1]+25),
        (pos[0]-25,pos[1]+25),
        (pos[0],pos[1]-5)
    ],0)

    sleep(10/1000)
    py.display.flip()