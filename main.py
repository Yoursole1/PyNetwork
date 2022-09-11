import random

from graphic.Board import Board
from neuralnet.Network import Network


def getRandom():
    a = list(range(10))
    output = []

    for i in range(2):
        output.append(random.choice(a))

    return output


def main():
    values = getRandom()
    networkA = Network([2, 2])
    networkB = Network([2, 2])

    print(networkA.calcOutputs(values))
    print(networkB.calcOutputs(values))
    print("------")
    networkC = networkA.breed(networkB)
    print(networkA.calcOutputs(values))
    print(networkB.calcOutputs(values))
    print(networkC.calcOutputs(values))



if __name__ == "__main__":
    main()
