import math

from entity.Creature import Creature
from entity.Food import Food
from graphic.graphics import *
from neuralnet.Network import Network


def distanceSquared(creature: Creature, food: Food):
    return (creature.getX() - food.getX()) ** 2 + (creature.getY() - food.getY()) ** 2  # TODO investigate this later


class Board:

    def __init__(self, creatures: int, width: int = 10, height: int = 10):
        self.win = None

        self.tileSize = 30

        self.squareWidth = width
        self.squareHeight = height

        self.pixelWidth = self.squareWidth * self.tileSize
        self.pixelHeight = self.squareHeight * self.tileSize

        self.creatures = []
        for i in range(creatures):
            self.creatures.append(
                Creature(Network([width * height, 100, 100, 100, 4]), self.squareWidth, self.squareHeight,
                         self.tileSize))

        self.food = []
        self.food.append(Food(self.squareWidth, self.squareHeight, self.tileSize))

        self.initialDist = {}
        for creature in self.creatures:
            self.initialDist[creature] = distanceSquared(creature, self.food[0])

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

        for epoch in range(1, 10000):  # generations (epoch)
            for i in range(50):  # steps

                for creature in self.creatures:
                    creature.draw(self.win)
                    creature.decideWhereToGo(self.generateInputs(creature))

                for food in self.food:
                    food.draw(self.win)

            newCreatures = []

            outputs = {}
            for creature in self.creatures:
                outputs[creature] = distanceSquared(creature, self.food[0])  # closer
                # creatures did better, hence
                # they are selected for
                # TODO make better fitness function because rn creatures that spawn far away make more "foward progress" so are ranked higher

            outputs = {k: v for k, v in sorted(outputs.items(), key=lambda item: item[1], reverse=False)}
            creatureA = list(outputs.keys())[0]
            creatureB = list(outputs.keys())[1]

            print(outputs[creatureA])

            for i in range(len(self.creatures)):
                newCreatures.append(creatureA.breed(creatureB, epoch))

            for creature in self.creatures:
                creature.undraw()

            self.creatures = newCreatures
            for creature in self.creatures:
                self.initialDist[creature] = distanceSquared(creature, self.food[0])

            self.food[0].undraw()
            self.food[0] = Food(self.squareWidth, self.squareHeight, self.tileSize)
            # time.sleep(0.1)

    def generateInputs(self, creature: Creature):
        l0 = [0] * (self.squareWidth * self.squareHeight)

        l0[self.convert(creature.getX(), creature.getY())] = creature.getWeight()
        for food in self.food:
            l0[self.convert(food.getX(), food.getY())] = food.getWeight()

        return l0

    def convert(self, x: int, y: int):  # assuming x and y are within valid boundaries
        x /= self.tileSize
        y /= self.tileSize
        val = y * self.squareWidth
        val += x
        return int(val)
