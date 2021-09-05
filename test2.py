import pygame
import pygame_essentials
import random

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')
mainclock = pygame.time.Clock()

heights = [720]*width

grains = []
running = True
r = 100
g = 100
b = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        if not r == 255 or g == 255 or b == 255:
            chosen_color = random.choice(['r','g','b'])
            if chosen_color == 'r':
                r += 10
                r %= 255
            if chosen_color == 'g':
                g += 1
                g %= 255
            if chosen_color == 'b':
                b += 1
                b %= 255
        else:
            chosen_color = random.choice(['r','g','b'])
            if chosen_color == 'r':
                r -= 10
                r %= 255
            if chosen_color == 'g':
                g -= 1
                g %= 255
            if chosen_color == 'b':
                b -= 1
                b %= 255
        p = pygame_essentials.Object('s', pygame.mouse.get_pos(), (r,g,b), 1)
        grains.append(p)
    screen.fill((0,0,0))
    for p in grains:
        p.draw(screen)
        moveable = True
        for x in range(-p.radius, p.radius):
            x += p.x
            if p.y + p.radius == heights[x] - p.radius:
                heights[x] -= (p.radius*2)
                moveable = False
        if (p.y < heights[x] - p.radius) and moveable:
            p.move(0,1)


    pygame.display.flip()
    mainclock.tick(80)