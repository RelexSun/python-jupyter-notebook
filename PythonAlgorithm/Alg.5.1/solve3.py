def binsearch(x, n, S) :
    low, high = 0, n - 1
    cnt = 0
    while low <= high :
        mid = (low + high) // 2
        cnt += 1
        if x == S[mid] :
            return cnt
        elif x < S[mid] :
            high = mid - 1
        else :
            low = mid + 1
    return cnt

def solve(n, m, S, X) :
    total = 0
    for i in range(m) :
        total += binsearch(X[i], n, S)
    print(total)
    
N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)