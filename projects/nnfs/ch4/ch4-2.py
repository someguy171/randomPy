# using ReLU with the dense layer code

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

X, y = spiral_data(samples=100, classes=3)
dense1 = Layer_Dense(2, 3)

# instantiate activation
activation1 = Activation_ReLU()

dense1.forward(X)

# apply ReLU to the values calculated for the neurons in the layer
activation1.forward(dense1.output)

print(activation1.output[:5])