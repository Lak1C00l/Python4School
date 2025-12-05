import pygame as py

WHITE = (255,255,255,)

class Car(py.sprite.Sprite):
    def __init__(self, color,width,height):

        super().__init__()


        # create image of 'car' and fill with color
        # you can also load image from disk
        self.image = py.Surface((width,height))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # draw rectangle on surface
        py.draw.rect(self.image, color ,[0,0, width,height])
        #Fetch images rectangle for mods
        self.rect = self.image.get_rect()

    def moveRight(self,pixals):
        self.rect.x += pixals

    def moveLeft(self,pixals):
        self.rect.x -= pixals

    def moveUp(self,pixals):
        self.rect.y -= pixals

    def moveDown(self,pixals):
        self.rect.y += pixals

    