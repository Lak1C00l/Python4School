import pygame as py
from car import Car
import sys
from time import sleep

RED = 255,0,0
PURPLE = 128,0,128


py.init()
width,height = 400,400
screen = py.display.set_mode((width,height))

# create sprite group
all_sprites = py.sprite.Group()
# make 2 instances of car
car1 = Car(RED,20,30)
car1.rect.x = 200
car1.rect.y = 300

car2 = Car(PURPLE,20,30)
car2.rect.x = 100
car2.rect.y = 100
#Adding car sprites to list of objects
all_sprites.add(car1)
all_sprites.add(car2)

while True:
    screen.fill([0,0,0])
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    # gets all keys currently pressed since last chack 
    keys = py.key.get_pressed()
    #dectect collision of 2 x
    collide = car1.rect.colliderect(car2.rect)

    if collide:
        car1.rect.x = 200
        car1.rect.y = 200
        car2.rect.x = 100
        car2.rect.y = 200
    else:

        if keys[py.K_LEFT]:
            car1.moveLeft(5)
        if keys[py.K_RIGHT]:
            car1.moveRight(5)
        if keys[py.K_UP]:
            car1.moveUp(5)
        if keys[py.K_DOWN]:
            car1.moveDown(5)

        if keys[py.K_a]:
            car2.moveLeft(5)
        if keys[py.K_d]:
            car2.moveRight(5)
        if keys[py.K_w]:
            car2.moveUp(5)
        if keys[py.K_s]:
            car2.moveDown(5)

    all_sprites.update()
    all_sprites.draw(screen)
    py.display.update()
    sleep(10/1000)
