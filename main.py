import random

from graphic.Board import Board
from neuralnet.Network import Network


def getRandom():
    a = [0, 1]
    output = []

    for i in range(2):
        output.append(random.choice(a))

    return output


def train():  # trains the network to output small values
    networks = []

    amountOfNetworks = 100
    for i in range(amountOfNetworks):
        networks.append(Network([2, 10, 1]))

    for epoch in range(1, 1000):
        inputs = getRandom()

        outputs = {}
        for network in networks:
            outputs[network] = network.calcOutputs(inputs)

        for key, value in outputs.items():
            outputs[key] = sum(value) / len(value)

        # sort based on how good it is at predicting 1/2 inputs[0]
        target = inputs[0] and inputs[1]
        for key, value in outputs.items():
            outputs[key] = (value - target) ** 2

        outputs = {k: v for k, v in sorted(outputs.items(), key=lambda item: item[1], reverse=False)}

        netA = list(outputs.keys())[0]
        netB = list(outputs.keys())[1]

        newNetworks = []
        for i in range(amountOfNetworks):
            newNetworks.append(netA.breed(netB, epoch))

        networks = newNetworks
        print(sum(networks[0].calcOutputs(inputs)) / len(networks[0].calcOutputs(inputs)))
    print(networks[0].calcOutputs([1, 1]))
    print(networks[0].calcOutputs([0, 1]))
    print(networks[0].calcOutputs([1, 0]))
    print(networks[0].calcOutputs([0, 0]))

    print(networks[0].toString())


def main():
    b = Board(50, 30, 30)
    b.draw()
    # train()

    # network = Network([2, 2])
    # print(network.toString())
    # print(network.calcOutputs([0, 0]))


if __name__ == "__main__":
    main()
