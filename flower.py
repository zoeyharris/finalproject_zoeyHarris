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

    return True


def draw_flower(screen, flower):
    x = flower["x"]
    y = flower["y"]
    growth = flower["growth"]
    petals = flower["petals"]
    petal_color = flower["color"]

    #stem 
    stem_height = int(growth * 2)
    pygame.draw.line(
        screen,
        STEM_GREEN,
        (x, y),
        (x, y - stem_height),
        4
    )

    #flower center position
    center_x = x
    center_y = y - stem_height

    # petal size 
    petal_distance = int(growth * 0.6)
    petal_radius = max(4, int(growth * 0.3))
    center_radius = max(5, int(growth * 0.25))

    #draw petals in a circle
    for i in range(petals):
        angle = (2 * math.pi / petals) * i
        petal_x = center_x + int(math.cos(angle) * petal_distance)
        petal_y = center_y + int(math.sin(angle) * petal_distance)

        pygame.draw.circle(
            screen,
            petal_color,
            (petal_x, petal_y),
            petal_radius
        )

    # draw center
    pygame.draw.circle(
        screen,
        CENTER_BROWN,
        (center_x, center_y),
        center_radius
    )

    #optional leaf
    leaf_y = y - stem_height // 2
    pygame.draw.ellipse(
        screen,
        STEM_GREEN,
        (x + 5, leaf_y, 18, 10)
    )


def draw_screen(screen, flowers):
    #background sky
    screen.fill(SKY_BLUE)

    #grass
    pygame.draw.rect(screen, GRASS_GREEN,  (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    


