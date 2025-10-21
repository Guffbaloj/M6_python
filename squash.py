import sys
import threading
import math
import time

from ball import Ball

input_char = None

WIDTH = 50
HEIGHT = 30

players = [[0,14],[59,14]]
ball = Ball([30,14],1,players,(WIDTH,HEIGHT))

def background_input():
    while True:
        global input_char
        input_char = input("")





def drawScreen(positionsList, ballPos):
    print(f"\n"*10)
    print(input_char)
    for y in range(WIDTH):
        row = ""
        for x in range(HEIGHT):
            if [x,y] == [round(ballPos[0]), round(ballPos[1])]:
                row += "o"
            elif [x,y] in positionsList:
                row += "I"
            else:
                row += " "
        print(row)
    print(ballPos)




background_input_thread = threading.Thread(target=background_input)
background_input_thread.start()

while True:
    drawScreen(players,ball.pos)
    ball.update()
    time.sleep(0.1)

