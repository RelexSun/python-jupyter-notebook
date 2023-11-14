def min_prime_factor(n) :
    mpf = [i for i in range(n + 1)]
    for i in range(2, int(n**0.5) + 1) :
        if mpf[i] == i :
            for j in range(i * i, n + 1, i) :
                if mpf[j] == j :
                    mpf[j] = i
    return mpf

def count_factor(n, mpf) :
    cnt = 0
    while n != 1 :
        cnt += 1
        n //= mpf[n]
    return cnt

def solve(n) :
    mpf = min_prime_factor(n)
    maxcnt = 0
    for i in range(2, n + 1) :
        maxcnt = max(maxcnt, count_factor(i, mpf))
    print(maxcnt)

N = int(input())
solve(N)