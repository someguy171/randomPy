# matrix product in numpy

import numpy as np

a = [[1, 2, 3, 4],
     [2, 3, 4, 5],
     [3, 4, 5, 6]]

b = [[2, 3, 4],
     [3, 4, 5],
     [4, 5, 6],
     [5, 6, 7]]

print(np.dot(a,b))