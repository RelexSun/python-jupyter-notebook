def solve(n, k, s) :
    d = {s[i]:k-s[i] for i in range(n)}
    for i in range(n) :
        if d[s[i]] in d and i < s.index(d[s[i]]) :
            print(s[i], d[s[i]])

N, K = map(int, input().split())
S = list(map(int, input().split()))
solve(N, K, S)