from pygame import *
from pygame.math import Vector2
from gamesprite import *
from const import *
class Player(Gamesprite):
    def __init__(self, img, x, y, size, speed =SPEED):
        super().__init__(img, x, y, size)
        self.speed = speed
        self.acc = 1
        self.dec = 2
        self.maxspeed = speed
        self.v = Vector2(0,0)
        self.pos = Vector2(x,y)
        self.lastpos=self.pos
        self.imageleft=transform.flip(self.image, True, False)
        self.imageright=self.image
    def getdirection(self, left=K_a, right=K_d):
        keys = key.get_pressed()
        direction = Vector2(0,0)
        if keys[left]:
            direction.x-=GAZAN
            self.image=self.imageleft
        if keys[right] :
            direction.x+=GAZAN
            self.image=self.imageright
        return direction
    
    def collide_walls_x(self, wall):
        if sprite.collide_mask(self, wall):
            step = 1.0 if self.v.x > 0 else -1.0
            # Откатываем назад по 1 пикселю, пока коллизия не исчезнет
            for _ in range(int(abs(self.v.x)) + 3):
                if not sprite.collide_mask(self, wall):
                    break
                self.pos.x -= step
                self.rect.centerx = int(self.pos.x)
            self.v.x = 0
    
    def collide_walls_y(self, wall):
        if sprite.collide_mask(self, wall):
            step = 1.0 if self.v.y > 0 else -1.0
            for _ in range(int(abs(self.v.y)) + 3):
                if not sprite.collide_mask(self, wall):
                    break
                self.pos.y -= step
                self.rect.centery = int(self.pos.y)
            self.v.y = 0
    def updatepony(self, window_rect, left=K_a, right=K_d):
        direction = self.getdirection(left, right)

        # Физика: ускорение и инерция
        if direction.length() > 0:
            direction.normalize_ip()
            self.v += direction * self.acc
        else:
            if self.v.length_squared() > 0:
                if self.v.length() < self.dec:
                    self.v = Vector2(0, 0)
                else:
                    self.v -= self.v.normalize() * self.dec

        if self.v.length_squared() > self.maxspeed**2:
            self.v.scale_to_length(self.maxspeed)

        self.pos.x += self.v.x
        self.rect.centerx = int(self.pos.x)

        self.pos.y += self.v.y
        self.rect.centery = int(self.pos.y)

        self.rect.clamp_ip(window_rect)
        self.pos.x, self.pos.y = self.rect.center

