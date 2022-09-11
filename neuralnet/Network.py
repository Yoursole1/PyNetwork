from neuralnet.Layer import Layer


class Network:

    def __init__(self, layerSizes: []):
        self.layers = []
        for i in range(len(layerSizes)-1):
            self.layers.append(Layer(layerSizes[i], layerSizes[i + 1]))

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

    def breed(self, other):
        if not self.isIsomorphic(other):
            raise Exception()

        for i in range(len(self.layers)):
            self.layers[i] = self.layers[i].breed(other.layers[i])

        return self

