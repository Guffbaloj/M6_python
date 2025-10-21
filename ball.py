import math
import pygame
class Ball:
    def __init__(self, pos:tuple, speed, displaySize, players:list):
        self.pos = pygame.math.Vector2(pos)
        self.velocity = pygame.math.Vector2(speed,4)
        self.speed = speed
        self.color = (233,233,88)
        self.displaySize = displaySize
        self.players = players
    def setPosition(self, newPos:tuple):
        self.pos = pygame.math.Vector2(newPos)
    def hasCollided(self):
        for player in self.players:
            if player.getRect().collidepoint(self.pos):
                return True
        #sedan lite väggkollition och sånt
        return False
            

    def move(self, steps):
        xstep = self.velocity.x/steps
        ystep = self.velocity.x/steps
        
        for _ in range(steps):
            self.pos.x + xstep
            if self.hasCollided():
                self.velocity.x *= -1
                
        for _ in range(steps):
            self.pos.y + ystep
            if self.hasCollided():
                self.velocity.y *= -1
                

    def render(self, display):
        pygame.draw.circle(display, self.color,self.pos,4)
       
    def update(self):
        self.move(self.speed)
    