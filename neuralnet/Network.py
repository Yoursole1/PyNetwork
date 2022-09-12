import copy

from neuralnet.Layer import Layer


class Network:

    def __init__(self, layerSizes: [], layers=None):
        if layers is None:
            layers = []

        self.layers = layers
        self.layerSizes = layerSizes
        if len(self.layers) == 0:
            for i in range(len(layerSizes) - 1):
                self.layers.append(Layer(layerSizes[i], layerSizes[i + 1]))

    def toString(self):
        finalString = ""
        for layer in self.layers:
            finalString += layer.toString() + "////"
        return finalString

    def calcOutputs(self, inputs: []):
        for layer in self.layers:
            inputs = layer.transform(inputs)
        return inputs

    def evaluate(self, inputs: []):
        outputs = self.calcOutputs(inputs)
        maximum = -999999999999
        index = -1

        for i in range(len(outputs)):
            if outputs[i] > maximum:
                maximum = outputs[i]
                index = i

        return index

    def isIsomorphic(self, other):
        works = True
        for i in range(len(self.layers)):
            if not self.layers[i].isIsomorphic(other.layers[i]):
                works = False
        return works

    # Returns a NEW network with the bred values
    def breed(self, other, epoch):
        if not self.isIsomorphic(other):
            raise Exception()

        layers = copy.deepcopy(self.layers)

        for i in range(len(self.layers)):
            layers[i] = self.layers[i].breed(other.layers[i], epoch)

        return Network(self.layerSizes, layers)

    def mutate(self, epoch):
        layers = copy.deepcopy(self.layers)

        for i in range(len(self.layers)):
            layers[i] = self.layers[i].mutate(epoch)

        return Network(self.layerSizes, layers)
