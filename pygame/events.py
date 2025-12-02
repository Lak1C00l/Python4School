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
crosshair = pygame.image.load("crosshair.png")
#scaling and transforming image
crosshair = pygame.transform.scale(crosshair, (50,40))
#getting image rectangle
crosshairRect = crosshair.get_rect()

#setting image speed
pos = [0,0]
#set tabby position

while True:
    screen.fill(backroundColor)
    #put image on screen
    screen.blit(crosshair,crosshairRect)

    pygame.display.flip()
    sleep(5/1000)