def solve(n) :
    cnt = 0
    for c in range((n+1)//3, (n+1)//2) :
        for b in range((n-c+1)//2, c+1) :
            cnt += 1
    return cnt

N = int(input())
print(solve(N))