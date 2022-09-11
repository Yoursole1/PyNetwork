import random
import math


def sigmoid(value: float):
    return 1 / (1 + math.exp(-1 * value))


class Layer:

    def __init__(self, inputCount: int, outputCount: int):
        self.inputCount = inputCount
        self.outputCount = outputCount
        self.weights = [[random.random() for _ in range(self.inputCount)] for _ in range(self.outputCount + 1)]
        self.biases = [random.random() for _ in range(self.outputCount)]

    def transform(self, inputs: []):
        outputs = []

        for nodeOut in range(self.outputCount):
            weightedOutput: float = self.biases[nodeOut]

            for nodeIn in range(self.inputCount):
                weightedOutput += inputs[nodeIn] * self.weights[nodeOut][nodeIn]

            outputs.append(sigmoid(weightedOutput))

        return outputs

    def breed(self, other):
        for i in range(len(self.biases)):
            val1 = self.biases[i]
            val2 = other.biases[i]

            # randomly pick one (recombination in life)

            selected = random.choice([val1, val2])

            # mutate 2% of the time
            mutateSelector = random.random()

            if mutateSelector < 0.02:
                selected += (random.random() - 0.5)
                selected = sigmoid(selected)

            self.biases[i] = selected

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

                self.weights[i][j] = selected

        return self

    def isIsomorphic(self, other):
        return self.inputCount == other.inputCount and self.outputCount == other.outputCount
