def find_primes(n):
    output = []
    sieve = [True] * (n+1)
    for num in range(2, n+1):
        if len(output) > 10001:
            return output[10000]
        if (sieve[num]):
            output.append(num)
            for kill in range(num, n+1, num):
                sieve[kill] = False

print(find_primes(1000000))