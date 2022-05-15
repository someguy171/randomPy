from math import sqrt, prod
import sys

squareList = [pow(x, 2) for x in range(1, 1000)]

for num1 in squareList:
    for num2 in squareList:
        add = num1 + num2
        for num3 in squareList:
            if (num3 == add) and (num1 < num2 < num3) and (sum([sqrt(num1), sqrt(num2), sqrt(num3)]) == 1000):
                print(prod([sqrt(num1), sqrt(num2), sqrt(num3)]))
                sys.exit()

