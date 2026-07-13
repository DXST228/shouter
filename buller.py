from pygame import *
from pygame.math import Vector2
from gamesprite import *
from const import *
from random import randint
class Bullet(Gamesprite):
    def __init__(self, img,x, y, size, speed =4):
        super().__init__(img,x, y, size)
        self.speed = speed
        self.run = False
        self.acc = 0.15
        self.dec = 0.3
        self.maxspeed = speed
        self.v = Vector2(0,0)
        self.pos = Vector2(0, 0)

    def update(self):
        if self.rect.y<=0:
            self.kill()      
        self.rect.y -= self.speed
    