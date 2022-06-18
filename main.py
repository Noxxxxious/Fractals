import pygame

SCREEN_H = 600
SCREEN_W = 800
pixel_color = (255, 255, 255)
center_x = int(SCREEN_W / 2)
center_y = int(SCREEN_H / 2)

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Sierpinski Fractals")

while True:
    surface.set_at((center_x, center_y), pixel_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
