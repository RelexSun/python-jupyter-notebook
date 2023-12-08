def solve(n, k, s) :
    for i in range(n) :
        for j in range(i + 1, n) :
            if s[i] + s[j] == k :
                print(s[i], s[j])

N, K = map(int, input().split())
S = list(map(int, input().split()))
solve(N, K, S)