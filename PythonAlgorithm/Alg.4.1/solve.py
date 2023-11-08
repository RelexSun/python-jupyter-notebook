def seqsearch(x, n, S):
    for i in range(n):
        if x == S[i]:
            return i
    return -1


def solve(n, m, S, X):
    for i in range(m):
        print(seqsearch(X[i], n, S), end=" ")
    print()


N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)
