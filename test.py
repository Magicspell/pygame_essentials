import pygame
from pygame_essentials import Object

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

test = Object('r', (100,100), (255,255,255), height=10, width=100)
test.draw(screen)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()