import pygame

from player import Player
from ball import Ball

pygame.init()

WIDTH = 640
HEIGHT = 460
FPS = 60

window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

playerNr = 0
players = [Player((50,HEIGHT-50),(70,20),(32,182,132)), 
           Player((310,HEIGHT-50),(70,20),(182,32,132))]
currentPlayer = players[playerNr]
ball = Ball((200,200),(WIDTH,HEIGHT),players)
scoreArea = pygame.rect.Rect(0,HEIGHT-20,WIDTH,20)

def renderScene(display):
    pygame.draw.rect(window,(233,12,12),scoreArea)
    for player in players:
        player.render(display)
    ball.render(display)
def updateEnts():
    for player in players:
        player.update()
    ball.update()
def handleKeypress(key,keydown):
    if key == pygame.K_a:
        currentPlayer.movement["right"] = keydown
    if key == pygame.K_d:
        currentPlayer.movement["left"] = keydown
def checkIfScored():
    if scoreArea.collidepoint(ball.pos):
        ball.setPosition((WIDTH/2,HEIGHT/2))
        ball.setVelocity((3,3))
        players[ball.activePlayer].score += 1
        print(f"Wow, player {2 - ball.activePlayer} scored!")
        print(f"current score: {players[0].score} | {players[1].score}")
def manageEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                global currentPlayer
                global playerNr
                currentPlayer.movement["left"] = False
                currentPlayer.movement["right"] = False
                playerNr = (playerNr + 1)%2
                currentPlayer = players[playerNr]
            handleKeypress(event.key, True)
        if event.type == pygame.KEYUP:
            handleKeypress(event.key, False)

ball.setVelocity((-1,-3))
while True:
    window.fill((255,255,255))
    manageEvents()
    updateEnts()
    checkIfScored()
    renderScene(window)
    pygame.display.update()
    clock.tick(FPS)
