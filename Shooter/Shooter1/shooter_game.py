import random

import pygame.time
from pygame import *
from Shooter.Shooter1.Player import Player
from Shooter.Shooter1.Enemy import Enemy, return_lost
from Bullet import Bullet
from Shooter.Shooter1.Kamni import Kamni
from random import randint

# создай окно игры
rocket = Player
window = display.set_mode((850, 600))
display.set_caption("Шутер")


# задай фон сцены
background = transform.scale(image.load("skala.jpg"), (850, 600))

x1, y1 = 50, 500
x2, y2 = 0, 0

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound("fire.ogg")

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.Sysfont('Arial', 36)

win = font.SysFont('Arial', 36)
lose = font.SysFont('Arial', 36)


rocket = Player("rocket.png", x1, y1, 10, (65, 65),window)
ufo = Enemy('ufo.png', random.randint(0+20, 850-85), y2, 2,(80, 65), window)
kamen = Kamni('asteroid.png', random.randint(0+20, 850-85), y2, 2,(80, 65), window)

score = 0
FPS = 60
clock = time.Clock()

fire_rate = 250
last_shot = pygame.time.get_ticks()

ufos = [Enemy('ufo.png', random.randint(0+20, 850-85), y2, 2,(80, 65), window) for i in range(5)]
kamni = [Kamni('asteroid.png', random.randint(0+20, 850-85), y2, 2,(80, 65), window) for i in range(3)]
monsters = sprite.Group()
bullets = sprite.Group()
kamnis = sprite.Group()

for i in range(5):
    monsters.add(ufos[i])

for i in range(3):
    kamnis.add(kamni[i])

game = True
finish = False
while game:
    # Установка ФПС
    clock.tick(FPS)

    text_lose = font1.render("Пропущено:" + str(return_lost()), 1, (255, 255, 255))
    text_kill = font2.render("Повержено:"+ str(score), 1, (255, 255, 255))


    for e in event.get():

        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))

        window.blit(text_lose, (0, 0))
        window.blit(text_kill, (0, 40))

        rocket.reset()
        rocket.update()

        bullets.draw(window)
        bullets.update()

        monsters.draw(window)
        monsters.update()

        kamnis.draw(window)
        kamnis.update()

        keys = key.get_pressed()
        if keys[K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - last_shot >= fire_rate:
                rocket.fire(bullets, fire)
                last_shot = current_time

        sprite_list1 = sprite.groupcollide(bullets, kamnis, True, True)
        for bullet in sprite_list1:
            kamnis.add(Kamni('asteroid.png', random.randint(0+20, 850-85), y2, 3,(80, 65), window))

        sprite_list = sprite.groupcollide(bullets, monsters, True, True)
        for bullet in sprite_list:
            score += len(sprite_list[bullet])
            monsters.add(Enemy('ufo.png', random.randint(0, 700), 0,
                               random.randint(1, 4), (65, 65), window))

        if score >= 10:
            finish = True
            win_game = font1.render("YOU WIN", 1, (255, 255, 255))
            window.blit(win_game, (250, 200))
        elif return_lost() >= 3 or sprite.spritecollide(rocket, monsters, False) or sprite.spritecollide(rocket, kamnis, False):
            finish = True
            loose_game = font1.render("YOU LOOSE", 1, (255, 255, 255))
            window.blit(loose_game, (250, 200))

    display.update()
    
