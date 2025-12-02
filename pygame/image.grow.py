import pygame
from time import sleep

#initalizing pygame
pygame.init()
width,height = 400, 400
backroundColor = 200,100,0
screen = pygame.display.set_mode((width,height))

#importing image
flatCat = pygame.image.load("Ginger Exotic Shorthair Cat.jpg")

#scaling and transforming image
flatCat = pygame.transform.scale(flatCat, (50,50))

#getting image rectangle
flatCatRect = flatCat.get_rect()

#setinital position
flatCatRect.left = 175
flatCatRect.top = 175
flatCatSize = [50,50]
direct = [2,2]
pos = [-1,-1]
while True:
    screen.fill(backroundColor)
    #put image on screen
    screen.blit(flatCat,flatCatRect)
    #
    flatCat = pygame.transform.scale(flatCat, flatCatSize)
    flatCatSize[0] += direct[0]
    flatCatSize[1] += direct[1]
    flatCatRect.left += pos[0]
    flatCatRect.right += pos[1]
    if flatCatSize[0] >= width:
        pos[0] = - pos[0]
        pos[1] = - pos[1]
        direct[0] = - direct[0]
        direct[1] = - direct[1]
    if flatCatSize[1] <= 50:
        pos[0] = - pos[0]
        pos[1] = - pos[1]
        direct[0] = - direct[0]
        direct[1] = - direct[1]

    pygame.display.flip()
    sleep(5/1000)