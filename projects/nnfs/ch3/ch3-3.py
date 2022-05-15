import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        # generate an array of random numbers with dimensions (no. of inputs, no. of neurons)
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        
        # generate an array of 0s, as long as the no. of neurons
        self.biases = np.zeros((1, n_neurons))
    
    def forward(self, inputs):
        # calculate the neurons' outputs, using a list of inputs passed in
        self.output = np.dot(inputs, self.weights) + self.biases

# generate random data (3 spirals of 100 samples each) - this data is coordinates (hence "X, y")
X, y = spiral_data(samples=100, classes=3)

# generate a dense layer (2 inputs, 3 neurons)
dense1 = Layer_Dense(2, 3)

# pass the generated data into the dense layer
dense1.forward(X)

print(dense1.output[:5])