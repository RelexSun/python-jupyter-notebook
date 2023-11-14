def find_primes(n) :
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**0.5) + 1) :
        if sieve[i] == 1 :
            for j in range(i + i, n + 1, i) :
                sieve[j] = 0
    return sieve

def solve(n) :
    sieve = find_primes(n) 
    return sum(sieve)

N = int(input())
print(solve(N))

