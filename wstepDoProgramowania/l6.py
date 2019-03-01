from math import sqrt
from random import uniform, getrandbits
from pylab import scatter, show
from l6_disc import Disc

class Board:

    def __init__(self, width=640, height=320, discs=[]):
        self.width = width
        self.height = height
        self.xRange = self.width/2-self.width, self.width/2
        self.yRange = self.height/2-self.height, self.height/2
        self.discs = discs

    def addDisc(self, disc):
        self.discs.append(disc)
        return self.discs

    def plot(self):
        X = [disc.x for disc in self.discs]
        Y = [disc.y for disc in self.discs]
        scatter(X,Y)
        show()

    def getRandomCoords(self):
        return uniform(*self.xRange), uniform(*self.yRange)

    @staticmethod    
    def collide(disc1, disc2):
        dist = sqrt(abs(disc1.x-disc2.x)**2+abs(disc1.y-disc2.y)**2)
        return dist < disc1.radius+disc2.radius

    def outOfBoard(self, disc):
        if disc.x > self.xRange[1] or disc.x < self.xRange[0] or disc.y < self.yRange[0] or disc.y > self.yRange[1]:
            return True
        else: return False

    def getCollisions(self, disc):
        sortByY = lambda d: d.y
        discs = sorted(self.discs, key=sortByY)
        collisions = []
        for disc2 in discs:
            totalRadius = disc.radius+disc2.radius
            if disc.y+1 > disc2.y and disc.y-1 < disc2.y and disc != disc2:
                if self.collide(disc, disc2) and not [disc2, disc] in collisions:
                    dist = sqrt(abs(disc.x-disc2.x)**2+abs(disc.y-disc2.y)**2)
                    k = totalRadius/abs(dist-.001)
                    collisions.append([disc, disc2, k])
            elif self.outOfBoard(disc2):
                collisions.append([disc2, disc2, 0])
            else: continue
        return collisions

    def getAllCollisions(self):
        sortByY = lambda d: d.y
        discs = sorted(self.discs, key=sortByY)
        collisions = []
        for disc1 in discs:
            if len(self.getCollisions(disc1)) > 0:
                collisions.extend(self.getCollisions(disc1))
        return collisions
    
    def fixCollisions(self):
        cols = self.getAllCollisions()
        if len(cols) > 0:
            for col in cols:
                stepX = abs(col[0].x-col[1].x)*col[2]
                stepY = abs(col[0].y-col[1].y)*col[2]
                elIndex = self.discs.index(col[0])
                self.discs[elIndex].move([stepX, stepY])
                newCols = self.getCollisions(self.discs[elIndex])
                
                angle = 10
                while len(newCols) > 0:
                    for x in range(int(360/angle)):
                        self.discs[elIndex].rotateVector(angle)
                        newCols = self.getCollisions(self.discs[elIndex])

                    x, y = self.discs[elIndex].x, self.discs[elIndex].y
                    self.discs[elIndex].move([-x/3+self.xRange[1]/5, -y/3+1+self.yRange[1]/5])
                
                

    


def main():
    N = 100
    board = Board(30,30)
    for _ in range(N):
        coords = board.getRandomCoords()
        radius = 0.5
        board.addDisc(Disc(radius, coords))

    board.plot()
    while len(board.getAllCollisions())>0:
        print(len(board.getAllCollisions()))
        board.fixCollisions()
    board.plot()

main()