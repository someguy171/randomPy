# using softmax for output layer

import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        
class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

X, y = spiral_data(samples=100, classes=3)
dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()

# create an output layer, with three inputs (3 outputs from previous layer) and 3 outputs (3 classes of original data)
dense2 = Layer_Dense(3, 3)

# create softmax activation for output layer
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

# make a forward pass using the previous layer's output
dense2.forward(dense1.output)

# make a forward pass through the activation function
activation2.forward(dense2.output)

print(activation2.output[:5])