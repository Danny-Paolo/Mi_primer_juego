import sys
from player import Player
from enemies import Enemies
from clouds import Clouds
from settings import Settings
import pygame

class PYGAME_INIT():
    def __init__(self) :
        pygame.init()
        # Inicio sonido
        pygame.mixer.init()

        # Configuraciones de pantalla
        self.SCREEN_BG = (135, 206, 250)
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screenWidth = self.screen.get_rect().width
        self.screenHeight = self.screen.get_rect().height

        # Configuraciones de sonido
        self.sonido = pygame.mixer.Sound("./sound/sound_play.mp3")
        # -1 sonido se reproduza indefinidamente
        pygame.mixer.Sound.play(self.sonido,-1)

        self.running = True

        # Clases de otros componentes
        self.player = Player(self)
        self.settings = Settings()

        # Sprites
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()

        # Creando tiempo muestre el enemigo
        self.ADDENEMIE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMIE,700)

        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD,1200)

    # Dibuja objetos
    def add_sprite_screen(self):
        # Añadiendo player sprites
        self.all_sprite_list.add(self.player)
        # Dibuja player y enemies en pantalla
        for attr in self.all_sprite_list:
            self.screen.blit(attr.surf,attr.rect)

    def design_screen(self):
        self.screen.fill(self.SCREEN_BG)
        self.add_sprite_screen()
        self.settings.CLOCK = 20
        # Actualiza pantalla
        pygame.display.flip()

    def get_keys(self):
        pressed_keys = pygame.key.get_pressed()
        self.player.update(pressed_keys)

    # Detectando collision
    def collision(self):
        if pygame.sprite.spritecollideany(self.player,self.enemies):
            self.player.kill()
            self.running = False

    # Creando enemigos
    def create_Enemie(self):
        new_enemie = Enemies(self)
        self.enemies.add(new_enemie)
        self.all_sprite_list.add(new_enemie)

    # Creando nubes
    def create_Clouds(self):
        new_cloud = Clouds(self)
        self.clouds.add(new_cloud)
        self.all_sprite_list.add(new_cloud)

    # Generamos eventos
    def event_get(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            elif event.type == self.ADDENEMIE:
                self.create_Enemie()


            elif event.type == self.ADDCLOUD:
                self.create_Clouds()

        # Movimiento sprits
        self.enemies.update()
        self.clouds.update()

    def main(self):
        while self.running:
            self.event_get()
            self.design_screen()
            self.get_keys()
            self.collision()

if __name__ == "__main__" :
    init = PYGAME_INIT()
    init.main()
    # print(init.ene.rect)
