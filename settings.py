import random
import time
import pygame

class Settings():
    def __init__(self) :
        self.SPEED_PLAYER = 2
        self.SPEED_ENEMIES = random.uniform(2,4)
        self.SPEED_CLOUDS = 1.5
        # Tiempo de procesamiento
        self.CLOCK = time.process_time()        

