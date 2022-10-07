import pygame
import random
from settings import Settings

class Clouds(pygame.sprite.Sprite):
    def __init__(self, main) :
        super().__init__()
        self.main = main
        self.surf = pygame.image.load("./img/cloud.png")
        self.surf_height = self.surf.get_rect().height
        self.center=(
                random.randint(self.main.screenHeight, self.main.screenWidth),
                random.randint(self.surf_height,(self.main.screenHeight-self.surf_height)) 
        )
        self.rect = self.surf.get_rect(center=(self.center))
        self.set = Settings()

    def update(self):
        self.rect.move_ip(-self.set.SPEED_CLOUDS,0)
        if self.rect.right < 0:
            self.kill()
