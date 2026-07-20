from pygame import *
from const import *
from gamesprite import *
from player import *
from enemy import *
from random import choice
from bonus import *
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
    bonus = Bonus(BONUS,K_SIZE, 10)
    boss = Player(BOSS,0, -BOSS_SIZE[1], BOSS_SIZE)

    return(ship, monsters, bonus)


font.init()
title=font.SysFont('verdana', 36)
small=font.SysFont('verdana', 25)

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


ship, monsters, bonus = give_birth()


record=title.render('Красавчик, но мог быстрее ',True, PINK)
i =0
game= True
finish = False
iswin = True
while game:
    if not finish:
        if ship.hasupgrade: 
            ship.bonustime-=1
            if ship.bonustime <=0:
                ship.hasupgrade=False
                ship.bonustime=BONUSTIME*FPS
        # отобразить картинку фона
        background.draw(window)
        score=small.render(f'счет {ship.score}',True, WHITE)
        antiscore=small.render(f'счет {ship.antiscore}',True, WHITE)
        window.blit(score, (10,10))
        window.blit(antiscore, (10,40))
        ship.draw(window)
        ship.updatepony(window.get_rect())
        ship.bullets.draw(window)
        ship.bullets.update()
        #ship.drawrect(window)
        monsters.draw(window)
        monsters.update(ship)
        bonus.draw(window)
        bonus.update()

            
        #if sprite.collide_rect(ship, fluttershy):
            #ship.draw(window)
            #finish = True

    #         ball.speed_y *= -1
        if sprite.spritecollide( ship,monsters, True):
            iswin = False
            finish = True
        for  c in sprite.groupcollide(monsters, ship.bullets, True, True):
            img = choice(list(MONSTERS.keys()))
            monster = Enemy(img, MONSTERS[img], 3)
            monsters.add(monster) 
            ship.score += 1
        if sprite.collide_rect(ship, bonus):
            bonus.spawn()
            bonus.iswaiting=True
            ship.hasupgrade= True
            print(ship.bonustime)
        if ship.score >= MAXMONSTERS:
            for monster in monsters:
                monster.kill()

            
        
            
    else: 
        if not iswin:
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
