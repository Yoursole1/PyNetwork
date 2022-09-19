import random
from abc import ABC, abstractmethod

from graphic.graphics import GraphWin


class GameObject(ABC):

    def __init__(self, width: int, height: int, tileSize: int):
        self.xLoc = random.choice(list(range(width))) * tileSize
        self.yLoc = random.choice(list(range(height))) * tileSize

    @abstractmethod
    def draw(self, win: GraphWin):
        pass

    @abstractmethod
    def getWeight(self):
        pass

    def getX(self):
        return self.xLoc

    def getY(self):
        return self.yLoc
