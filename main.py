import random

from graphic.Board import Board
from neuralnet.Layer import Layer
from neuralnet.Network import Network
import copy


def getRandom():
    a = list(range(10))
    output = []

    for i in range(2):
        output.append(random.choice(a))

    return output


def main():
    network = Network([2, 2])

    for i in range(100000):
        networkB = Network([2,2])
        randomVals = getRandom()
        if sum(networkB.calcOutputs(randomVals))/len(networkB.calcOutputs(randomVals)) < sum(network.calcOutputs(randomVals))/len(network.calcOutputs(randomVals)):
            network = network.breed(networkB)

    print(network.calcOutputs(getRandom()))



if __name__ == "__main__":
    main()
