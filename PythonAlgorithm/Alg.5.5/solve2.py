def binsearch(n, s) :
    low, high = 0, n - 1
    while low < high :
        mid = (low + high) // 2    
        if s[mid] % 2 == 0 : # even
            high = mid
        else : # odd
            low = mid + 1
    return -1 if s[low] % 2 == 1 else low

def solve(n, s) :
    j = binsearch(n, s)
    print(0 if j < 0 else s[j])
    
N = int(input())
S = list(map(int, input().split()))
solve(N, S)