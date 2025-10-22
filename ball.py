import math
import pygame
class Ball:
    def __init__(self, pos:tuple, speed, displaySize, players:list,activePlayer):
        self.pos = pygame.math.Vector2(pos)
        self.velocity = pygame.math.Vector2(speed,2)
        self.speed = speed
        self.color = (233,233,88)
        self.displaySize = displaySize
        self.players = players
        self.activePlayer = activePlayer
    def setVelocity(self, newVel:tuple):
        self.velocity = pygame.math.Vector2(newVel)
    def setPosition(self, newPos:tuple):
        self.pos = pygame.math.Vector2(newPos)
    
    def hasCollided(self):
        player = self.players[self.activePlayer]
        if player.getRect().collidepoint(self.pos):
            self.activePlayer = self.activePlayer + 1 % 2
            return True
        if self.pos.x < 0 or self.pos.x > self.displaySize[0]:
            return True
        if self.pos.y < 0 or self.pos.y > self.displaySize[1]:
            return True
        return False
            

    def move(self, steps):
        xstep = self.velocity.x/steps
        ystep = self.velocity.y/steps
        
        for _ in range(steps):
            self.pos.x += xstep
            if self.hasCollided():
                self.pos.x -= xstep
                self.velocity.x *= -1
                break
        for _ in range(steps):
            self.pos.y += ystep
            if self.hasCollided():
                self.pos.y -= ystep
                self.velocity.y *= -1
                break
                

    def render(self, display):
        pygame.draw.circle(display, self.color,self.pos,5)
       
    def update(self):
        self.move(self.speed)
    