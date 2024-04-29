from pygame import *
from GameSprite import GameSprite
from Shooter.Shooter1.Bullet import Bullet
class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 850 - 80:
            self.rect.x += self.speed

    def fire(self, group, sound):
        group.add(Bullet('bullet.png', self.rect.x+27, self.rect.y-15, 10, (15, 15), self.window))
        sound.play()