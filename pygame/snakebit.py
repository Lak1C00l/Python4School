import pygame as py

WHITE = (255,255,255)
width, height = 10,10

"""
Author: Lara Atanasova
Date Modified: December 5th
"""

class SnakeBit(py.sprite.Sprite):
    def __init__(self, color,x,y):
        # inits parent clas aka Pygame Sprite
        super().__init__()
        self.color = color
        #make surface to draw sprite
        self.image = py.Surface((width,height))
        self.image.fill(WHITE)
        #draw rect
        py.draw.rect(self.image, color,[0,0,width,height])
        #settting intit position for rect
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def moveUp(self,pixels):
        self.rect.centery -= pixels
    def moveDown(self,pixals):
        self.rect.centery += pixals
    def moveRight(self,pixels):
        self.rect.centerx += pixels
    def moveLeft(self,pixels):
        self.rect.centerx -= pixels

