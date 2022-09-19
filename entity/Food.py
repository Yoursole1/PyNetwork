from abc import ABC

from entity.GameObject import GameObject
from graphic.graphics import Rectangle, GraphWin, Point


class Food(GameObject, ABC):

    def __init__(self, width: int, height: int, tileSize: int):
        super().__init__(width, height, tileSize)
        self.sq = None

        self.width = width
        self.height = height

        self.tileSize = tileSize

    def draw(self, win: GraphWin):
        if not (self.sq is None):
            self.sq.undraw()
        self.sq = Rectangle(Point(self.xLoc, self.yLoc), Point(self.xLoc + self.tileSize, self.yLoc + self.tileSize))
        self.sq.setFill("red")
        self.sq.draw(win)

    def undraw(self):
        self.sq.undraw()

    def getWeight(self):
        return -1
