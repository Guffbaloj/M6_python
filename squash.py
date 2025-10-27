import pygame
import server
import time

from player import Player
from ball import Ball

pygame.init()

WIDTH = 640
HEIGHT = 460
FPS = 60

amITheServer = False

window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

players = [Player((50,HEIGHT-50),(70,20),(32,182,132), True),
           Player((310,HEIGHT-50),(70,20),(182,32,132), False)]
localPlayer = players[0]
ball = Ball((200,200),(WIDTH,HEIGHT),players)
scoreArea = pygame.rect.Rect(0,HEIGHT-20,WIDTH,20)

def renderScene(display):
    pygame.draw.rect(window,(233,12,12),scoreArea)
    for i in range(len(players)):
        players[i].render(display, i == ball.activePlayer)
    ball.render(display)
def updateEntities():
    for player in players:
        player.update()
    if amITheServer:
        ball.update()
def handleKeypress(key,keydown):
    if key == pygame.K_a:
        localPlayer.movement["right"] = keydown
    if key == pygame.K_d:
        localPlayer.movement["left"] = keydown
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
            handleKeypress(event.key, True)
        if event.type == pygame.KEYUP:
            handleKeypress(event.key, False)

playerJoinedYet = False
def netMessageHandler(msg):
    if msg.get_type() == server.MESSAGE_PLAYER_JOIN:
        global playerJoinedYet
        if not amITheServer:
            print("?????? En tredje spelare gick med ??????")
        playerJoinedYet = True
    elif msg.get_type() == server.MESSAGE_PLAYER_MOVE:
        players[1].setPosition((msg.x, msg.y))
    elif msg.get_type() == server.MESSAGE_BALL_MOVE:
        ball.setPosition((msg.x, msg.y))
    elif msg.get_type() == server.MESSAGE_BALL_ACTIVE_PLAYER:
        # player ids är olika på server och klient
        ball.activePlayer = 1 - msg.player

i = input("Vill du starta klient eller server? ")
if i[0].lower() == 'k':
    pygame.display.set_caption("Squash - Klient")
    host = input("Vem vill du ansluta till (till exempel 100.74.124.97)? ")
    server.start_client(host, netMessageHandler)
    while server.connection == None:
        time.sleep(0.1)
elif i[0].lower() == 's':
    pygame.display.set_caption("Squash - Server")
    amITheServer = True
    server.start_server(netMessageHandler)
    print("Väntar på att en spelare ska gå med...")
    while not playerJoinedYet:
        time.sleep(0.5)
    print("En spelare gick med! Spela på!")
else:
    print("Kom tillbaka när du har bestämt dig för att vara antingen klient eller server!")
    exit()

ball.setVelocity((-1,-3))
while True:
    window.fill((255,255,255))
    manageEvents()
    updateEntities()
    if amITheServer:
        checkIfScored()
    renderScene(window)
    pygame.display.update()
    clock.tick(FPS)
