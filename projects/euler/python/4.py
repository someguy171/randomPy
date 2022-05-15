# problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0

for c1 in range(100, 1000):
    for c2 in range(100, 1000):
        palin = c1 * c2
        if str(palin) == str(palin)[::-1]:
            if palin > largest:
                largest = palin

print(largest)