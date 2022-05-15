# problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 7, 9, 11, 13, 16, 17, 19, 20

num = 20

while (num % 7 != 0) or (num % 9 != 0) or (num % 11 != 0) or (num % 13 != 0) or (num % 16 != 0) or (num % 17 != 0) or (num % 19 != 0):  
    num += 20
print(num)
