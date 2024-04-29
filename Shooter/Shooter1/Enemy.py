import random
from pygame import *
from GameSprite import GameSprite
from random import randint

lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 700:
            self.rect.y = 0
            self.rect.x = random.randint(0+20, 850-85)
            self.speed = random.randint(1, 4)
            lost += 1

def return_lost():
    global lost
    return lost







