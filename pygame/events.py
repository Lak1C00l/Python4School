import pygame as py

py.init()

import pygame
from time import sleep

#initalizing pygame
pygame.init()
width,height = 700, 700
backroundColor = 200,100,0
screen = pygame.display.set_mode((width,height))


#importing image
crosshair = pygame.image.load("pygame/crosshair.png")
#scaling and transforming image
crosshair = pygame.transform.scale(crosshair, (50,40))
#getting image rectangle
crosshairRect = crosshair.get_rect()
print(crosshairRect.center)
#setting image speed
pos = [200,200]
while True:
    screen.fill(backroundColor)
    #put image on screen
    crosshairRect.center = pos
    screen.blit(crosshair,crosshairRect)

    for event in py.event.get():
        if event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                pos = [crosshairRect.center[0]-5,crosshairRect.center[1]]
            if event.key == py.K_RIGHT:
                pos = [crosshairRect.center[0]+5,crosshairRect.center[1]]
            if event.key == py.K_UP:
                pos = [crosshairRect.center[0],crosshairRect.center[1]-5]
            if event.key == py.K_DOWN:
                pos = [crosshairRect.center[0],crosshairRect.center[1]+5]

    pygame.display.flip()
    sleep(5/1000)