import math

# problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

target = 600851475143
largest = 0
check = 2

while (check < math.sqrt(target)):
    # if target is divisible by the check
    if target % check == 0:
        # divide the target
        target = target / check
        # record the check
        largest = check
    # if target is not divisible by the check
    else:
        # increment the check
        check += 1

if (target > largest):
    largest = target

print(largest)