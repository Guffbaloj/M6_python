import pygame

from player import Player
from ball import Ball

pygame.init()

WIDTH = 480
HEIGHT = 360
FPS = 60

window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

playerNr = 0
players = [Player((50,240),(70,20),(32,132,32)), 
           Player((310,240),(70,20),(132,32,32))]
currentPlayer = players[playerNr]
ball = Ball((200,200),40,(WIDTH,HEIGHT),players)

def renderPlayers(display):
    for player in players:
        player.render(display)

def updatePlayers():
    for player in players:
        player.update()

def handleKeypress(key,keydown):
    if key == pygame.K_a:
        currentPlayer.movement["right"] = keydown
    if key == pygame.K_d:
        currentPlayer.movement["left"] = keydown

while True:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            handleKeypress(event.key, True)
        if event.type == pygame.KEYUP:
            handleKeypress(event.key, False)

    updatePlayers()
    ball.update()

    renderPlayers(window)
    ball.render(window)
    pygame.display.update()
    clock.tick(FPS)
