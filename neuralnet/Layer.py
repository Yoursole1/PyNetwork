import random
import math
import copy


def sigmoid(value: float):
    return 1 / (1 + math.exp(-1 * value))


class Layer:

    def __init__(self, inputCount: int, outputCount: int, weights=None, biases=None):
        if biases is None:
            biases = []
        if weights is None:
            weights = []

        self.inputCount = inputCount
        self.outputCount = outputCount
        if len(weights) == 0 and len(biases) == 0:
            self.weights = [[random.random() for _ in range(self.inputCount)] for _ in range(self.outputCount + 1)]
            self.biases = [random.random() for _ in range(self.outputCount)]
        else:
            self.weights = weights
            self.biases = biases

    def transform(self, inputs: []):
        outputs = []

        for nodeOut in range(self.outputCount):
            weightedOutput: float = self.biases[nodeOut]

            for nodeIn in range(self.inputCount):
                weightedOutput += inputs[nodeIn] * self.weights[nodeOut][nodeIn]

            outputs.append(sigmoid(weightedOutput))

        return outputs

    def breed(self, other):
        weights = copy.deepcopy(self.weights)
        biases = copy.deepcopy(self.biases)

        for i in range(len(self.biases)):
            val1 = copy.deepcopy(self.biases[i])
            val2 = copy.deepcopy(other.biases[i])

            # randomly pick one (recombination in life)

            selected = random.choice([val1, val2])

            # mutate 2% of the time
            mutateSelector = random.random()

            if mutateSelector < 0.02:
                selected += (random.random() - 0.5)
                selected = sigmoid(selected)

            biases[i] = selected

        for i in range(len(self.weights)):
            for j in range(len(self.weights[0])):
                val1 = self.weights[i][j]
                val2 = other.weights[i][j]

                # randomly pick one (recombination in life)

                selected = random.choice([val1, val2])

                # mutate 2% of the time
                mutateSelector = random.random()

                if mutateSelector < 0.02:
                    selected += (random.random() - 0.5)
                    selected = sigmoid(selected)

                weights[i][j] = selected

        return Layer(self.inputCount, self.outputCount, weights, biases)

    def isIsomorphic(self, other):
        return self.inputCount == other.inputCount and self.outputCount == other.outputCount
