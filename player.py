import pygame

class Player:
    def __init__(self, pos:tuple, size: tuple, color):
        self.pos = pygame.math.Vector2(pos)
        self.size = pygame.math.Vector2(size)
        self.color = color
        self.speed = 2
    
    def getRect(self):
        rect = pygame.rect.Rect(0,0,self.size[0], self.size[1])
        rect.center = self.pos
        return rect
    
    def move(self, upp, down):
        self.pos[0] += (down - upp) * self.speed
    def update(self):
        ...
    
    def render(self, display):
        pygame.draw.rect(display, self.color, self.getRect())
