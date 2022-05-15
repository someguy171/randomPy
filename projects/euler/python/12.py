import sys
import math 

# problem 12

for x in range(2, 20000):
    num = sum([y for y in range(1, x+1)])
    sqrt = round(math.sqrt(num))
    count = 0
    if sqrt * sqrt == num:
        count -= 1
    for x in range(1, sqrt):
        if num % x == 0:
            count += 2
            if count > 500:
                print(num)
                sys.exit()