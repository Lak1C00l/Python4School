import pygame as py
import sys
from time import sleep
from snakebit import SnakeBit as bit
from foodSprite import Food

#initalizing pygame interface
py.init()

# screen dimensions
SCREENWIDTH = 400
SCREENHEIGHT = 400
#total screen size
size = (SCREENWIDTH,SCREENHEIGHT)

#init py displace
screen = py.display.set_mode(size)
py.display.set_caption("Snake Game")

#Defining Colour Codes
GRAY = (101, 105, 112)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (91, 0, 166)
BLACK = (0, 0, 0)
YELLOW = (255, 191, 0)
PALE_RED = (240, 115, 115)
WEIRD_YELLOW = (238, 255, 0)
BLUE = (3, 3, 252)
PINK = (255, 0, 157)
colours = [
    GREEN, RED, BLACK, YELLOW, BLUE, WEIRD_YELLOW, PINK, PALE_RED, PURPLE
]

#create sprite groups
snakeBod = py.sprite.Group()
foodGroup = py.sprite.Group()

#creating stating sprites
firstSnake  = bit(BLUE,200,200)
snakeBod.add(firstSnake)

#make food
food = Food(GREEN,100,100)
foodGroup.add(food)


gameOn = True
pixelMove = 10
key = 0
while gameOn:


    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                key = 2
            if event.key == py.K_UP:
                key = 1
            if event.key == py.K_LEFT:
                key = 4
            if event.key == py.K_RIGHT:
                key = 3
    if key !=0:
        if key ==1:
            firstSnake.moveUp(pixelMove)
        elif key ==2:
            firstSnake.moveDown(pixelMove)
        elif key ==3:
            firstSnake.moveRight(pixelMove)
        elif key ==4:
            firstSnake.moveLeft(pixelMove)
    #update sprite groups
    snakeBod.update()
    foodGroup.update()

    # filling screen and displaying
    screen.fill(GRAY)

    #drawing sprites on screen
    snakeBod.draw(screen)
    foodGroup.draw(screen)

    py.display.update()
    sleep(50/1000)

