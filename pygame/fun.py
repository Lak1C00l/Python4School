import pygame as py
from time import sleep
from random import randint

py.init()

length,width = 600,600
screen = py.display.set_mode((width,length))
colors = randint(0,255),randint(0,255),randint(0,255)

pushen = py.image.load("pygame/pusheen.jpg")
pushen= py.transform.scale(pushen, (100,100))
pushenRect = pushen.get_rect()
pushenSleep = py.image.load("pygame/pusheenLyingDown.jpg")
pushenSleep = py.transform.scale(pushenSleep, (100,100))
pushenSleepRect = pushenSleep.get_rect()

pushenSleepRect.left = 250
pushenSleepRect.top = 250
pushenRect.left = 250
pushenRect.top = 250

pos = [200,200]

while True:

   
    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                newColors = randint(0,255),randint(0,255),randint(0,255)
                screen.fill(newColors)
                screen.blit(pushen,pushenRect)
                
        if event.type == py.KEYUP:
            pushenRect.center = pos
            screen.blit(pushenSleep,pushenSleepRect)


    py.display.flip()
    sleep(5/1000)

