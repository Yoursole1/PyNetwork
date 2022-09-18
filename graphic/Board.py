from entity.Creature import Creature
from graphic.graphics import *
from neuralnet.Network import Network


class Board:

    def __init__(self, creatures: int, width: int = 10, height: int = 10):
        self.win = None

        self.tileSize = 70

        self.squareWidth = width
        self.squareHeight = height

        self.pixelWidth = self.squareWidth * self.tileSize
        self.pixelHeight = self.squareHeight * self.tileSize

        self.creatures = []
        for i in range(creatures):
            self.creatures.append(Creature(Network([width*height, 100, 100, 50, 4]), self.squareWidth, self.squareHeight, self.tileSize))

    def draw(self):
        self.win = GraphWin("My Little Block World!", width=self.pixelWidth,
                            height=self.pixelHeight)

        self.win.setBackground(color="green")

        for i in range(self.tileSize, self.pixelWidth, self.tileSize):
            line = Line(Point(i, 0), Point(i, self.pixelHeight * self.tileSize))
            line.draw(self.win)

        for i in range(self.tileSize, self.pixelHeight, self.tileSize):
            line = Line(Point(0, i), Point(self.pixelHeight * self.tileSize, i))
            line.draw(self.win)

