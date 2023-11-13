def factorize(n):
    if n < 2:
        return []
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return [i] + factorize(n//i)
        return [n]


def solve(N):
    factors = factorize(N)
    print(" ".join(map(str, factors)))


N = int(input())
solve(N)
