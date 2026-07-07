from pygame import *
from const import *
from gamesprite import *
from player import *
from enemy import *
#from classes import*


def give_birth():
    ship = Player(SHIP,0,WIN_H-SHIP_SIZE[1], SHIP_SIZE)
    ship.pos.x=WIN_W//2
    ship.rect.centerx=WIN_W//2

    #fluttershy = Gamesprite(PONY1,(WIN_W-P1_SIZE[0])/2,WIN_H-70, P1_SIZE)
    monsters=sprite.Group()
    for img in MONSTERS :
        monster = Enemy(img, MONSTERS[img], 3)
        monsters.add(monster)
    #kluch = Gamesprite(KIUCH,WIN_W-K_SIZE[0], 10, K_SIZE)

    return(ship, monsters)


font.init()
title=font.SysFont('verdana', 36)
# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()

# название окна
display.set_caption("Я грр, ты мне?")

# задать картинку фона такого же размера, как размер окна
background = Gamesprite(FON, 0, 0, (WIN_W,WIN_H))


ship, monsters = give_birth()


record=title.render('Красавчик, но мог быстрее ',True, PINK)
i =0
game= True
finish = False
while game:
    if not finish:
        # отобразить картинку фона
        background.draw(window)
        ship.draw(window)
        ship.updatepony(window.get_rect())
        ship.bullets.draw(window)
        ship.bullets.update()
        #ship.drawrect(window)
        monsters.draw(window)
        monsters.update()

            
        #if sprite.collide_rect(ship, fluttershy):
            #ship.draw(window)
            #finish = True

    #         ball.speed_y *= -1
    #     if sprite.spritecollide( ball,monsters, True):
    #         ball.speed_y *= -1
    else: 
        if sprite.collide_rect(ship, fluttershy):
            record=title.render('Красавчик ',True, PINK)
        else:
            record=title.render('Красавчик, но мог быстрее ',True, PINK)

        window.blit(record, (300,400))
        

    # слушать события и обрабатывать
    for e in event.get():
        if e.type == KEYDOWN: 
            if e.key == K_SPACE: 
                if not finish:
                    ship.shoot()
            if e.key == K_p: 
                if finish: 
                    ship, fluttershy, diskord, kluch = give_birth()
                    finish = False
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)
