import pygame as py

GRAY =(101,105,112)
width, height = 10,10

"""
Author: Lara Atanasova
Date Modified: December 5th
"""

class Food(py.sprite.Sprite):
    def __init__(self, color,x,y):
        # inits parent clas aka Pygame Sprite
        super().__init__()
        self.color = color
        #make surface to draw sprite
        self.image = py.Surface((width,height))
        self.image.fill(GRAY)
        #draw rect
        py.draw.circle(self.image, color,(5,5),5)
        #settting intit position for rect
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
