import pygame
from time import sleep

#initalizing pygame
pygame.init()
width,height = 700, 700
backroundColor = 200,100,0
screen = pygame.display.set_mode((width,height))
#importing image
flatCat = pygame.image.load("Ginger Exotic Shorthair Cat.jpg")
tabby = pygame.image.load("cat2.jpg")
#scaling and transforming image
flatCat = pygame.transform.scale(flatCat, (50,40))
tabby = pygame.transform.scale(tabby, (50,40))
#getting image rectangle
flatCatRect = flatCat.get_rect()
tabbyRect = tabby.get_rect()
#setting image speed
flatCatSpeed = [1,1]
tabbySpeed = [-1,1]
#set tabby position
tabbyRect.right = width
while True:
    screen.fill(backroundColor)
    #put image on screen
    screen.blit(flatCat,flatCatRect)
    screen.blit(tabby,tabbyRect)
    #move our image
    flatCatRect = flatCatRect.move(flatCatSpeed)
    tabbyRect = tabbyRect.move(tabbySpeed)
#changing direction when hit wall
    if flatCatRect.left<0 or flatCatRect.right>width:
        flatCatSpeed[0] = -flatCatSpeed[0]
    if flatCatRect.top<0 or flatCatRect.bottom> height:   
        flatCatSpeed[1] = -flatCatSpeed[1]

    if tabbyRect.left<0 or tabbyRect.right>width:
        tabbySpeed[0] = -tabbySpeed[0]
    if tabbyRect.top<0 or tabbyRect.bottom> height:   
        tabbySpeed[1] = -tabbySpeed[1]

    pygame.display.flip()
    sleep(5/1000)