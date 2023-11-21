def find_primes(n) :
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**0.5) + 1) :
        if sieve[i] == 1 :
            for j in range(i * i, n + 1, i) :
                sieve[j] = 0
    return [i for i in range(n) if sieve[i] == 1]

def binsearch(x, n, s) :
    low, high = 0, n - 1 
    while low <= high :
        mid = (low + high) // 2
        if x == s[mid] :
            return mid
        elif x < s[mid] :
            high = mid - 1
        else :
            low = mid + 1
    return -1

def solve(n, s, maxn) :
    primes = find_primes(maxn) 
    for i in range(n) :
        j = binsearch(s[i], len(primes), primes)
        print(j + 1, end=" ")
    print()

N = int(input())
S = list(map(int, input().split()))
solve(N, S, 100000)