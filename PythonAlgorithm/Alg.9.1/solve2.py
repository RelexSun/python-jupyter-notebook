def solve(a, b, m) :
    r = a
    for _ in range(b - 1) :
        r = r * a % m
    return r

A, B, M = map(int, input().split())
print(solve(A, B, M))