import sys
import threading
import math
import time
import pygame

input_char = None


players = [[0,4],[29,4]]
ball = [[15,4],math.pi,2]

def background_input():
    while True:
        global input_char
        input_char = input("")

def drawScreen(positionsList, ballPos):
    print(f"\n"*10)
    print(input_char)
    for y in range(10):
        row = ""
        for x in range(30):
            if [x,y] == [round(ballPos[0]), round(ballPos[1])]:
                row += "o"
            elif [x,y] in positionsList:
                row += "I"
            else:
                row += " "
        print(row)
    print(ballPos)

def updateBall(ball):
    ballX, ballY = ball[0] 
    ballDir = ball[1]
    ballSpeed = ball[2]

    for _ in range(ballSpeed):
        BOUNCE_ANGLE = math.pi + 0.05
        if ballX < 0:
            ballDir += BOUNCE_ANGLE
        if ballY < 0:
            ballDir += BOUNCE_ANGLE
        if ballX > 30:
            ballDir += BOUNCE_ANGLE
        if ballY > 10:
            ballDir += BOUNCE_ANGLE
        if [round(ballX), round(ballY)] in players:
            ballDir += BOUNCE_ANGLE
            print("oj")

        ballX += math.cos(ballDir)
        ballY += math.sin(ballDir)
    ball[0] = [ballX, ballY]
    ball[1] = ballDir
    print(ball)


background_input_thread = threading.Thread(target=background_input)
background_input_thread.start()

# while True:
#     drawScreen(players,ball[0])
#     updateBall(ball)
#     time.sleep(1)

WIN_WIDTH = 640
WIN_HEIGHT = 480
FPS = 60

# FIXME: ta bort om vi bestämmer oss för att slopa terminalgränssnittet!
def termpos2winpos(termpos):
    x,y = termpos
    return (x*WIN_WIDTH/30, y*WIN_HEIGHT/10)

def draw(surface):
    for p in players:
        winpos = termpos2winpos(p)
        r = pygame.Rect(winpos[0], winpos[1], 20, 80)
        pygame.draw.rect(surface, (255,255,255), r)
    ballpos = termpos2winpos(ball[0])
    pygame.draw.circle(surface, (255,255,255), ballpos, 5)

window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw(window)
    updateBall(ball)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
