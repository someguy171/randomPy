# finding the derivative in python

import numpy as np

# now, the function is non-linear
def f(x):
    return 2*x**2

# we can find the gradient of this line using a tangent
# take any value of x, and add a tiny tiny tiny tiny number to it
# now find the gradient using these two points, giving an approximation of the gradient of the tangent
# this is the "derivative"

# this tiny value is typically 0.0001
p2_delta = 0.0001

x1 = 1
x2 = x1 + p2_delta

y1 = f(x1)
y2 = f(x2)

approx_derivative = (y2-y1)/(x2-x1)
print(approx_derivative)