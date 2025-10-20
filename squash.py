import sys
import threading
import math
import time

input_char = None


players = [[0,4],[29,4]]
ball = [[15,4],math.pi,2]

def background_input():
    while True:
        global input_char
        input_char = input("")

background_input_thread = threading.Thread(target=background_input)
background_input_thread.start()



def drawScreen(positionsList, ballPos):
    print(f"\n"*10)
    print(input_char)
    for y in range(10):
        row = ""
        for x in range(30):
            if [x,y] == [int(ballPos[0]), int(ballPos[1])]:
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
        if [int(ballX), int(ballY)] in players:
            ballDir += math.pi
            print("oj")

        ballX += math.cos(ballDir)
        ballY += math.sin(ballDir)
        print(int(ballX), int(ballY))
    ball[0] = [round(ballX), round(ballY)]
    ball[1] = ballDir


while True:
    drawScreen(players,ball[0])
    updateBall(ball)
    time.sleep(1)

