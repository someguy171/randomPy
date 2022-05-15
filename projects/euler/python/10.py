def find_primes(n):
    output = []
    sieve = [True] * (n+1)
    for num in range(2, n+1):
        if (sieve[num]):
            output.append(num)
            for kill in range(num, n+1, num):
                sieve[kill] = False
    return output

print(sum(find_primes(2000000)))