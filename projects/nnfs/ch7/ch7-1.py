import py_compile
# finding the gradient of a line

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x

x = np.array(range(5))
y = f(x)

print(x)
print(y)

# find the gradient of the line using delta-y/delta-x
print((y[1]-y[0]) / (x[1]-x[0]))

plt.plot(x, y)
plt.show()