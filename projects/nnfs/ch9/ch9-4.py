x = [1.0, -2.0, 3.0]    # input values
w = [-3.0, -1.0, 2.0]   # weights
b = 1.0                 # bias

# assume these have been found from ch9-3
# these are the partial derivatives of ReLU with respect to the weights
dw = [1.0, -2.0, 3.0]
# this is the partial derivative of ReLU with respect to the bias
db = 1.0

# these are gradients, which show the direction of the steepest ascent
# we want loss to decrease, so we reverse the sign to go down instead
w[0] += -0.001 * dw[0]
w[1] += -0.001 * dw[1]
w[2] += -0.001 * dw[2]
b += -0.001 * db
print(w, b)

# backpropagation has found the effect the weights have on the output
# by changing the weights by a proportion of this effect, we can intelligently adjust to reduce loss
# this can be seen by performing another forward pass, which shows a change in the output (6 to 5.985)

# Multiplying inputs by weights
xw0 = x[0] * w[0]
xw1 = x[1] * w[1]
xw2 = x[2] * w[2]

# Adding
z = xw0 + xw1 + xw2 + b
# ReLU activation function
y = max(z, 0)
print(y)