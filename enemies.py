import pygame
import random
from settings import Settings

class Enemies(pygame.sprite.Sprite):
    def __init__(self,main) :
        super().__init__()
        self.main = main
        self.surf = pygame.image.load("./img/enemie.png").convert_alpha()
        # No desborde enemigo de la pantalla
        self.surf_height = self.surf.get_rect().height
        self.surf.set_colorkey((255,255,255))
        self.center=(
                random.randint(self.main.screenHeight, self.main.screenWidth),
                random.randint(self.surf_height,(self.main.screenHeight-self.surf_height)) 
        )
        self.rect = self.surf.get_rect(center=(self.center))
        self.spd = Settings()

    def update(self):
        self.rect.move_ip(-self.spd.SPEED_ENEMIES,0)
        if self.rect.right < 0 :
            self.kill()