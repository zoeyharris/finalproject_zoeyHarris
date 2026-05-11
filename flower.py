import pygame
import random
import math

#screen settings
WIDTH = 800
HEIGHT = 600
SKY_BLUE = (200, 230, 255)
GRASS_GREEN = (170, 220, 140)
STEM_GREEN = (40, 140, 70)
CENTER_BROWN = (120, 80, 40)


def setup_screen():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Procedural Flower Garden")
    return screen


def create_clock():
    return pygame.time.Clock()


def close_program():
    pygame.quit()


def create_seed(x, y):
    return {
        "x": x,
        "y": y,
        "growth": 5,
        "max_growth": random.randint(30, 60),
        "petals": random.randint(6, 12),
        "color": random.choice([
            (255, 105, 180), #pink
            (255, 182, 193), #light pink
            (255, 215, 0),   #yellow
            (186, 85, 211),  #purple
            (255, 140, 0),   #orange
            (255, 99, 71)    #coral
        ]),
        "grown": False

    }