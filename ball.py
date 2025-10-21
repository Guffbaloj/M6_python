import math
class Ball:
    def __init__(self, pos:list, speed:int, players:list, sceneSize:tuple):
        self.dir = math.pi
        self.pos = pos
        self.speed = speed
        self.players = players
        self.sceneWidth = sceneSize[0]
        self.sceneHeight = sceneSize[1]
    
    def update(self):
        ballX, ballY = self.pos
        for _ in range(self.speed):
            BOUNCE_ANGLE1 = math.pi + math.pi/8
            BOUNCE_ANGLE2 = math.pi/4
            if ballX < 0:
                self.dir += BOUNCE_ANGLE1
            if ballY < 0:
                self.dir += BOUNCE_ANGLE2
            if ballX >= self.sceneWidth:
                self.dir += BOUNCE_ANGLE1
                ballX = self.sceneWidth
            if ballY >= self.sceneHeight:
                self.dir += BOUNCE_ANGLE2
                ballY = self.sceneHeight
            if [round(ballX), round(ballY)] in self.players:
                self.dir += BOUNCE_ANGLE1

            ballX += math.cos(self.dir)
            ballY += math.sin(self.dir)
        self.pos = [ballX, ballY]
        self.dir = self.dir
        print(self.pos)