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


def grow_flower(flower):
    if flower["gorwth"] < flower["max_growth"]:
        flower["growth"] += 0.3
    else:
        flower["grown"] = True


def update_flowers(flowers):
    for flower in flowers:
        grow_flower(flower)


def handle_events(flowers):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            #only plant flowers in the grass area 
            if y > HEIGHT // 2:
                flowers.append(create_seed(x, y))