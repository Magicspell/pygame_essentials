import pygame
import pygame_essentials

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shadows')
mainclock = pygame.time.Clock()

obstacles = []
o = pygame_essentials.Object('s', (100,100), (100,100,100), radius=100)
obstacles.append(o)
o = pygame_essentials.Object('s', (300,400), (100,100,100), radius=50)
obstacles.append(o)
o = pygame_essentials.Object('s', (700,400), (100,100,100), radius=30)
obstacles.append(o)
o = pygame_essentials.Object('s', (800,120), (100,100,100), radius=100)
obstacles.append(o)

light = pygame_essentials.Light(screen, (0,0), obstacles, brightness=60, color=(255,150,150))
light2 = pygame_essentials.Light(screen, (201,0), obstacles, brightness=10, color=(100,100,255))
light2.cast()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    light.loc = pygame.mouse.get_pos()
    light.cast()
    light.draw()
    light2.draw()
    for o in obstacles:
        o.draw(screen)
    pygame.display.flip()
    mainclock.tick(60)