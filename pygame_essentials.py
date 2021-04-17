import pygame


class Object():
    def __init__(self, type, loc, color, radius = None, height = None, width = None):
        if type == 'square' or type == 's':
            self.type = 's'
            self.radius = radius
        if type == 'circle' or type == 'c':
            self.type = 'c'
            self.radius = radius
        if type == 'rectangle' or type =='r':
            self.type = 'r'
            self.width = width
            self.height = height
        self.x = loc[0]
        self.y = loc[1]
        self.color = color
    def draw(self, screen):
        if self.type == 's':
            rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
            pygame.draw.rect(screen, self.color, rect)
        if self.type == 'c':
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.type == 'r':
            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, self.color, rect)

