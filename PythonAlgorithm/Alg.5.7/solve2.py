def cut(n, s, h) :
    # length = 0
    # for i in range(n) :
    #     length += (s[i] - h) if s[i] > h else 0
    # return length
    return sum([(s[i] - h) for i in range(n) if s[i] > h ])

def binsearch(n, M, s) :
    low, high = 0, max(s)
    while low < high :
        mid = (low + high) // 2
        if cut(n, s, mid) < M :
            high = mid
        else :
            low = mid + 1
    return low - 1


def solve(n, M, s) :
    j = binsearch(n, M, s)
    print(j)

N, M = map(int, input().split())
S = list(map(int, input().split()))
solve(N, M, S)