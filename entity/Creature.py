from entity.GameObject import GameObject
from graphic.graphics import GraphWin, Rectangle, Point
from neuralnet.Network import Network


class Creature(GameObject):

    def __init__(self, ai: Network, width: int, height: int, tileSize: int):
        super().__init__(width, height, tileSize)
        self.ai = ai

        self.width = width
        self.height = height

        self.tileSize = tileSize

        self.sq = None

        self.movements = ['l', 'r', 'u', 'd', 'n']

    def breed(self, other, epoch: int):
        return Creature(self.ai.breed(other.getAi(), epoch), self.width, self.height, self.tileSize)

    def getAi(self):
        return self.ai

    def decideWhereToGo(self, l0: []):
        movement = self.movements[self.ai.evaluate(l0)]
        self.move(movement)

    def move(self, direction: str):
        if direction == "u":
            if self.yLoc - self.tileSize < 0:
                return
            self.yLoc -= self.tileSize
        elif direction == "d":
            if self.yLoc + self.tileSize > self.height * self.tileSize - self.tileSize:
                return
            self.yLoc += self.tileSize
        elif direction == "r":
            if self.xLoc + self.tileSize > self.width * self.tileSize - self.tileSize:
                return
            self.xLoc += self.tileSize
        elif direction == "l":
            if self.xLoc - self.tileSize < 0:
                return
            self.xLoc -= self.tileSize
        elif direction == "n":
            pass

    def draw(self, win: GraphWin):
        if not (self.sq is None):
            self.sq.undraw()
        self.sq = Rectangle(Point(self.xLoc, self.yLoc), Point(self.xLoc + self.tileSize, self.yLoc + self.tileSize))
        self.sq.setFill("purple")
        self.sq.draw(win)

    def undraw(self):
        self.sq.undraw()

    def getWeight(self):
        return 1
