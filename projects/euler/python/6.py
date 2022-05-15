# problem 6

# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

total1 = sum([pow(x, 2) for x in range(1, 101)])
total2 = pow(sum(range(1, 101)), 2)

print(total2 - total1)