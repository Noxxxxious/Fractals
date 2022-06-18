import pygame
import math
import time
import random

SCREEN_H = 600
SCREEN_W = 800
center_x = int(SCREEN_W / 2)
center_y = int(SCREEN_H / 2)
icon = pygame.image.load("icon.png")
caption = "Fractals"

# modify this value to generate a different fractal
N = 6
PI = math.pi
R = 300
vertices = [(math.cos(2 * PI / N * x) * R + center_x, math.sin(2 * PI / N * x) * R + center_y) for x in range(0, N + 1)]


def two_random_adjacent_vertices():
    index = random.randint(0, N - 1)
    index2 = (index + 1) % N if random.randint(0, 1) else (index - 1) % N
    ver1 = vertices[index]
    ver2 = vertices[index2]
    return ver1, ver2


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def main():
    pygame.display.set_icon(icon)
    surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption(caption)
    prev_point = (center_x, center_y)
    while True:
        (v1, v2) = two_random_adjacent_vertices()
        new_point_x = round((v1[0] + v2[0] + prev_point[0]) / 3)
        new_point_y = round((v1[1] + v2[1] + prev_point[1]) / 3)
        surface.set_at((new_point_x, new_point_y), random_color())
        prev_point = (new_point_x, new_point_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()


main()
