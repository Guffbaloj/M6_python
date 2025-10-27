import math
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
        self.drawCount = 0

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

    def render(self, display, isTheSuperplayer):
        color = self.color
        if isTheSuperplayer:
            factor = (math.sin(self.drawCount/10)**2 + 1.5)/2
            def multclampfancai(v):
                return min(int(v*factor), 255)
            color = (multclampfancai(self.color[0]), multclampfancai(self.color[1]), multclampfancai(self.color[2]))
        pygame.draw.rect(display, color, self.getRect())
        self.drawCount += 1
