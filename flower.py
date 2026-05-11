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


