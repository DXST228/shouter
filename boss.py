from pygame import *
from pygame.math import Vector2
from gamesprite import *
from const import *
from random import randint
class Bonus(Gamesprite):
    def __init__(self, img, size, wait,iswaiting=True, speed =5):
        super().__init__(img,0, 0, size)
        self.speed = speed
        self.run = False
        self.acc = 0.15
        self.dec = 0.3
        self.maxspeed = speed
        self.v = Vector2(0,0)
        self.pos = Vector2(0, 0)
        self.wait=wait*FPS
        self.iswaiting = iswaiting
        self.timer = self.wait
        self.spawn()

    
    def spawn(self):
        x=randint(self.rect.width//2, WIN_W-int(self.rect.width*1.5))
        y=-self.rect.height
        self.pos.x=x
        self.pos.y=y
        self.rect.centerx = int(self.pos.x)
        self.rect.centery = int(self.pos.y)

    def update(self):
        if self.rect.centery>=WIN_H+self.rect.width :
            self.iswaiting = True
        if self. iswaiting:
            self.timer-=1
            if self.timer==0:
                self.timer=self.wait
                self.iswaiting=False
                self.spawn()
        else:       
            self.pos.y += self.speed
            self.rect.centery = int(self.pos.y)
    