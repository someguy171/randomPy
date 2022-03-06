# 

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**2

# creates an array from 0 to 5, with each value incrementing by 0.001
# this will create a much smoother graph than x = [0, 1, 2, 3, 4, 5]
x = np.arange(0, 5, 0.001)
y = f(x)
plt.plot(x, y)

colours = ["k", "g", "r", "b", "c"]

def approx_tangent_line(x, approx_derivative):
    return (approx_derivative*x) + c

for i in range(5):
    p2_delta = 0.0001
    x1 = i
    x2 = x1 + p2_delta
    y1 = f(x1)
    y2 = f(x2)

    approx_derivative = (y2-y1)/(x2-x1)
    # find the y-intercept by plugging in values into y=mx+c and rearranging
    c = y2 - approx_derivative*x2

    def tangent_line(x):
        return approx_derivative*x + c

    # plot the tangent
    # 0.9 more and less than the x value
    to_plot = [x1-0.9, x1, x2+0.9]
    # plot on the graph
    # x values = the list above
    # y values = the y returned by the function (since we've found derivative)
    plt.plot([point for point in to_plot], [approx_tangent_line(point, approx_derivative) for point in to_plot], c=colours[i])
    plt.scatter(x1, y1, c=colours[i])

    print("Approximate derivative for f(x)",
        f"where x = {x1} is {approx_derivative}")

plt.show()