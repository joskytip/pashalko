import random
from pygame import *
from GameSprite import GameSprite
from random import randint


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

