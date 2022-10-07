import pygame
from settings import Settings
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self,main):
        super().__init__()
        self.surf = pygame.image.load("./img/nav.png").convert_alpha()
        self.surf.set_colorkey((0,0,0),pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.main = main
        self.spd = Settings()

    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-self.spd.SPEED_PLAYER)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,self.spd.SPEED_PLAYER)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.spd.SPEED_PLAYER,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.spd.SPEED_PLAYER,0)
        
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.main.screenHeight:
            self.rect.bottom = self.main.screenHeight
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.main.screenWidth:
            self.rect.right = self.main.screenWidth