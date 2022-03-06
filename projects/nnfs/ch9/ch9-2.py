# backpropagating through a layer

### FORWARDS PASS ###

x = [1.0, -2.0, 3.0]    # input values
w = [-3.0, -1.0, 2.0]   # weights
b = 1.0                 # bias

# Multiplying inputs by weights
xw0 = x[0] * w[0]
xw1 = x[1] * w[1]
xw2 = x[2] * w[2]

# Adding weighted inputs and a bias
z = xw0 + xw1 + xw2 + b

# ReLU activation function
y = max(z, 0)




### BACKWARDS PASS ###

# derivative from the next layer, which already went through a backwards pass
dvalue = 1.0

# derivative of ReLU with respect to z (essentially the final answer, just before ReLU was applied), and the chain rule
# because z = the sum
dReLU_dz = dvalue * (1. if z > 0 else 0.)

# derivative of a sum is ALWAYS 1
dsum_dxw0 = 1

# therefore, when finding partial derivatives of ReLU with respect to the sum,
# we still just have 1 as the derivative
dReLU_dxw0 = dReLU_dz * dsum_dxw0

# repeat for all the sum (including the bias)
dsum_dxw1 = 1
dsum_dxw2 = 1
dsum_db = 1

dReLU_dxw1 = dReLU_dz * dsum_dxw1
dReLU_dxw2 = dReLU_dz * dsum_dxw2
dReLU_db = dReLU_dz * dsum_db

# remember that the partial derivative of a multiplication with respect to x, equals y (where f(x) = xy) and vice versa
# p.d. of multiplication (weight*input, in this case) with respect to input0, equals weight0
dmul_dx0 = w[0]
dmul_dx1 = w[1]
dmul_dx2 = w[2]

dReLU_dx0 = dReLU_dxw0 * dmul_dx0
dReLU_dx1 = dReLU_dxw1 * dmul_dx1
dReLU_dx2 = dReLU_dxw2 * dmul_dx2

dmul_dw0 = x[0]
dmul_dw1 = x[1]
dmul_dw2 = x[2]

dReLU_dw0 = dReLU_dxw0 * dmul_dw0
dReLU_dw1 = dReLU_dxw1 * dmul_dw1
dReLU_dw2 = dReLU_dxw2 * dmul_dw2

print(dReLU_dx0, dReLU_dw0, dReLU_dx1, dReLU_dw1, dReLU_dx2, dReLU_dw2)