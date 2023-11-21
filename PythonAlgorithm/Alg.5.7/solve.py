def binsearch(low, high, n, M, s) :
    if low >= high :
        return low - 1
    else :
        mid = (low + high) // 2
        if cut(n, s, mid) < M :
            return binsearch(low, mid, n, M, s)
        else :
            return binsearch(mid + 1, high, n, M, s)

def cut(n, s, h) :
    length = 0
    for i in range(n) :
        length += (s[i] - h) if s[i] > h else 0
    return length

def solve(n, M, s) :
    j = binsearch(0, max(s), n, M, s)
    print(j)
    
N, M = map(int, input().split())
S = list(map(int, input().split()))
solve(N, M, S)