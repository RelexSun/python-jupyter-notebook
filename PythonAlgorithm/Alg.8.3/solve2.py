def solve(n, k, s) :
    for i in range(n) :
        if k - s[i] in s and i < s.index(k - s[i]) :
            print(s[i], k - s[i])

N, K = map(int, input().split())
S = list(map(int, input().split()))
solve(N, K, S)