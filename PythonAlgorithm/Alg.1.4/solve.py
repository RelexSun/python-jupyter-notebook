def solve(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return (cnt)


N = int(input())
print(solve(N))

# --------------------------------------------------------------
# print(len([i for i in range(1, N + 1) if N % i == 0]))
# --------------------------------------------------------------
# div = list(x for x in map(lambda x : 8 % x == 0, range(1, 9)) if x )
# print(len(div))
