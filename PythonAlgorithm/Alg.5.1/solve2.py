def binsearch2(x, n, S) :
    low, high = 0, n - 1
    while low <= high :
        mid = (low + high) // 2
        if x == S[mid] :
            return mid
        elif x < S[mid] :
            high = mid -1 
        else :
            low = mid + 1
    return -1

def solve(n, m, S, X) :
    for i in range(m) :
        j = binsearch2(X[i], n, S)
        print(j, end=" ")
    print()

N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)