import pygame
import server

class Player:
    def __init__(self, pos:tuple, size: tuple, color, isLocal: bool):
        self.pos = pygame.math.Vector2(pos)
        self.size = pygame.math.Vector2(size)
        self.color = color
        self.speed = 5
        self.movement = {"left":False, "right":False}
        self.isLocal = isLocal
        self.score = 0

    def getRect(self):
        rect = pygame.rect.Rect(0,0,self.size.x, self.size.y)
        rect.center = self.pos
        return rect

    def setPosition(self, newPos:tuple):
        self.pos = pygame.math.Vector2(newPos)

    def update(self):
        self.pos.x += (self.movement["left"] - self.movement["right"])*self.speed
        if self.isLocal:
            server.send_message(server.connection, server.PlayerMoveMessage(self.pos.x, self.pos.y))

    def render(self, display):
        pygame.draw.rect(display, self.color, self.getRect())
