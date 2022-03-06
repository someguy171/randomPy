# intro to optimisation

from doctest import OutputChecker
import numpy as np
import nnfs
from nnfs.datasets import vertical_data
import comp

nnfs.init()

X, y = vertical_data(samples=100, classes=3)

# create the first layer - 2 inputs, 3 neurons
dense1 = comp.Layer_Dense(2, 3)
# create the ReLU activation fucntion for layer 1
activation1 = comp.Activation_ReLU()

# create the second layer - 3 inputs, 3 neurons
dense2 = comp.Layer_Dense(3, 3)
# create the softmax activation function for layer 2
activation2 = comp.Activation_Softmax()

# create the loss function
loss_function = comp.Loss_CategoricalCrossentropy()

# make some helper variables, to track the best (lowest) loss, and the weights / biases that gave us that loss
lowest_loss = 9999999                           # just some random number to start with
best_dense1_weights = dense1.weights.copy()     # copy() ensures an actual copy, not a reference to the object
best_dense1_biases = dense1.biases.copy()
best_dense2_weights = dense2.weights.copy()
best_dense1_biases = dense2.biases.copy()

for iteration in range(10000):
    # adjust weights incrementally each iteration
    dense1.weights += 0.05 * np.random.randn(2, 3)
    dense1.biases += 0.05 * np.random.randn(1, 3)
    dense2.weights += 0.05 * np.random.randn(3, 3)
    dense2.biases += 0.05 * np.random.randn(1, 3)
    
    # perform forward passes of the training data through both layers
    dense1.forward(X)                       # X is the input data (from the generated graph)
    activation1.forward(dense1.output)
    dense2.forward(activation1.output)
    activation2.forward(dense2.output)
    
    loss = loss_function.calculate(activation2.output, y)   # y is the target data

    predictions = np.argmax(activation2.output, axis=1)
    accuracy = np.mean(predictions == y)
    
    # if the new loss is better, report it back and rewerite the best weights/biases/losses
    if loss < lowest_loss:
        print("New set of weights found! Iteration:", iteration, "\nLoss:", loss, "\nAcc:", accuracy, "\n\n")
        best_dense1_weights = dense1.weights.copy()
        best_dense1_biases = dense1.biases.copy()
        best_dense2_weights = dense2.weights.copy()
        best_dense2_biases = dense2.biases.copy()
        lowest_loss = loss 
    # if the new loss is worse, revert values back a step, to try something different in the next iteration
    else:
        dense1.weights = best_dense1_weights.copy()
        dense1.biases = best_dense1_biases.copy()
        dense2.weights = best_dense2_weights.copy()
        dense2.biases = best_dense2_biases.copy()