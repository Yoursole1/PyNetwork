from graphic.graphics import *


class Board:

    def __init__(self, width: int = 10, height: int = 10):
        self.win = None
        self.width = width
        self.height = height

        self.tileSize = 10

    def draw(self):
        self.win = GraphWin("My Little Block World!", width=self.width * self.tileSize,
                            height=self.height * self.tileSize)

