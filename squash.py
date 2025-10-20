players = [[0,4],[29,4]]
ball = [15,4]

def drawScreen(positionsList, ballPos):
    print(f"\n"*10)
    for y in range(10):
        row = ""
        for x in range(30):
            if [x,y] == ballPos:
                row += "o"
            elif [x,y] in positionsList:
                row += "I"
            else:
                row += " "
        print(row)

drawScreen(players,ball)
