def solve(n) :
    cnt = 0
    for a in range(1, n) :
        for b in range(a, n) :
            for c in range(b, n) :
                if a + b + c == n and a + b > c :
                    cnt += 1
    return cnt

N = int(input())
print(solve(N))