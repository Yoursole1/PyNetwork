import random

from graphic.graphics import GraphWin
from neuralnet.Network import Network


class Creature:

    def __init__(self, ai: Network, width: int, height: int, tileSize: int):
        self.ai = ai
        self.xLoc = random.choice(list(range(width)))
        self.yLoc = random.choice(list(range(height)))

        self.width = width
        self.height = height

        self.tileSize = tileSize

    def breed(self, other, epoch: int):
        return Creature(self.ai.breed(other.getAi(), epoch), self.width, self.height, self.tileSize)

    def getAi(self):
        return self.ai

    def getX(self):
        return self.xLoc

    def getY(self):
        return self.yLoc

    def move(self, direction: str):
        if direction == "u":
            self.yLoc -= 1
        elif direction == "d":
            self.yLoc += 1
        elif direction == "r":
            self.xLoc += 1
        elif direction == "l":
            self.xLoc -= 1

    def draw(self, win: GraphWin):
        pass
