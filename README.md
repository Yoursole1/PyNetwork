# PyNetwork


## Authors

- [@Yoursole1](https://github.com/Yoursole1)

## What is this project?

This is my first attempt at looking into Genetic Algorithms
for training a population of "creatures" to optimize a task
within a grid.  

The stages:
-
- Create a basic network capable of calculating outputs
- Create a genetic algoithm that uses a fitness function
- Test it on basic boolean logic (2 inputs 1 output)
- Test with compositions of boolean logic (3+ inputs)
- Create a GUI that "creatures" can eat "food" squares

Current Version:
-
**The network:**

Currently, the network uses a convolutional neural network 
([CNN Wiki](https://en.wikipedia.org/wiki/Convolutional_neural_network)) 
that takes the grid of cells as an input, and outputs 5 values from
0 to 1 (compressed with a sigmoid activation function).  It is also 
important to note that I used the ReLU activation function for the 
boolean logic, because its linearity made it better for the task.

Below are the two functions that were used as activation functions.

```python
def sigmoid(value: float):
    return 1 / (1 + math.exp(-1 * value))


def relu(value: float):
    if value > 0:
        return value
    else:
        return 0
```

The first training example worked through the process of Genetic Learning 
([GL Wiki](https://en.wikipedia.org/wiki/Genetic_algorithm)).  The network
had 1 input, 0 hidden layers, and 1 output.  The fitness function
rewarded networks that divide the input by two, and output 1/2(input).
This was easily reached, with the value of the weight converging to 0.5
and the value of the output layer's bias to 0.  This makes sense of course,
because multiplying the input by 0.5 is dividing by two.  

Next, I trained it to learn the average of two numbers.  This is 
non-trivial, like the previous training goal.  This is because 
the nature of the transformation between network layers, adding two 
numbers is something that can only be approximated.  This network had 
the structure 2->10->1 (2 inputs, 10 nodes in the first hidden layer, and 1 output).
For this, I used the relu activation function also because averaging 
two numbers usually results in a number greater than 1.  Note that this
choice in activation function does remove the possibility of averaging
negative numbers, however given that this was just an experiment it 
wasn't a focus.  I trained the network on two random numbers between 
1 and 20, and tested using random numbers between 30 and 100.  The error
was on average +-0.1.

With this success, I moved to boolean logic, which was a final test
of this network, which it passed easily.  


**The Genetic Algorithm:**

This algoithm uses a cost function (which acts a fitness function).
For the practice examples, the cost function was the standard one
used in networks learning with back propagation:  The sum of the 
squared differences between the desired output and the actual output 
of each output node.  For the final one, for each creature I took 
their distance from the food (smaller = better).  *This method has issues*, 
because if a creature randomly spawns near food then doesn't move, 
it will be selected for, but then the next generation simply
won't like moving, however it worked decently.  For both cost functions,
I simply sorted the networks (or creatures), from smallest to largest cost function, 
then bred the top two to create the next generation.  

The breeding works by randomly choosing one of each weight or bias
from each network.  This ensures that weights and biases don't 
change their location in the network, which would be unpredictable and 
inhibit learning.  If both networks are extreamly similar, this 
"recombination" (as it is called in sexual reproduction in life),
has little effect because all the weights and biases are similar, 
so randomly choosing one or the other often doesn't change much.  
This is why there is also a chance of mutation (currently set at 1% per
weight or bias).  The mutation "amount" is a value between -0.5 and 0.5,
which is then divided by the epoch (generation number), to make sure 
large destructive changes aren't made to the network in later stages
of evolution.  The mutations create genetic diversity, and 
are essential for "learned behaiviors" to evolve. 

Here is the mutation code for the biases:

```python
for i in range(len(self.biases)):
    val1 = copy.deepcopy(self.biases[i])
    val2 = copy.deepcopy(other.biases[i])

    # randomly pick one (recombination in life)
    selected = random.choice([val1, val2])

    # determines if a mutation happens
    mutate = random.random()

    if mutate < mutationRate:
        selected += (random.random() - 0.5) / epoch

        biases[i] = selected
```
**The GUI (World for the creatures):**

