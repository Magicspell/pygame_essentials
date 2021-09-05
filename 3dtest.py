import pygame_essentials as pe
import pygame


(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('3d')
mainclock = pygame.time.Clock()

objects = []
o = pe.ThreeDimObject('s', (width/2, height/2, 1), (255,0,0), radius=10)
objects.append(o)
o = pe.ThreeDimObject('s', (400, 500, 10), (150,100,0), radius=10)
objects.append(o)
o = pe.ThreeDimObject('c', (700, 300, 10), (0,0,255), radius=10)
objects.append(o)
o = pe.ThreeDimObject('r', (100, 300, 10), (140,0,150), width=10, height=50)
objects.append(o)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        for o in objects:
            o.z += 1
    if pressed[pygame.K_s]:
        for o in objects:
            o.z -= 1
    if pressed[pygame.K_a]:
        for o in objects:
            o.x += 1
    if pressed[pygame.K_d]:
        for o in objects:
            o.x -= 1
    screen.fill((0,0,0))
    for o in objects:
        o.draw(screen)
    pygame.display.flip()
    mainclock.tick(60)