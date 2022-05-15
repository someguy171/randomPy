# finding partial derivatives in one neuron

x = [1.0, -2.0, 3.0]    # input values
w = [-3.0, -1.0, 2.0]   # weights
b = 1.0                 # bias

# emulate a forward pass for one neuron
# first, multiply weight by input
xw0 = x[0] * w[0]
xw1 = x[1] * w[1]
xw2 = x[2] * w[2]
print(xw0, xw1, xw2)

# sum the products, and add the bias
z = xw0 + xw1 + xw2 + b

# apply ReLU activation
z = max(z, 0)
print(z)