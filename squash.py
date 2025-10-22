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
players = [Player((50,HEIGHT-50),(70,20),(32,132,32)), 
           Player((310,HEIGHT-50),(70,20),(132,32,32))]
currentPlayer = players[playerNr]
ball = Ball((200,200),4,(WIDTH,HEIGHT),players,activePlayer=0)
scoreArea = pygame.rect.Rect(0,HEIGHT-20,WIDTH,20)

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
def checkIfScored():
    if scoreArea.collidepoint(ball.pos):
        ball.setPosition((WIDTH/2,HEIGHT/2))
        ball.setVelocity((3,3))
        players[ball.activePlayer].score += 1
        print(f"Wow, player {2 - ball.activePlayer} scored!")
        print(f"current score: {players[0].score} | {players[1].score}")
        
ball.setVelocity((0,-3))
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
    
    checkIfScored()
    
    renderPlayers(window)
    ball.render(window)
    pygame.draw.rect(window,(233,12,12),scoreArea)
    pygame.display.update()
    clock.tick(FPS)
