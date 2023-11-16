def binsearch(n, s) :
    low, high = 0, n - 1
    mid = (low + high) // 2
    while mid != 0 and mid != n - 1 :
        mid = (low + high) // 2
        if s[mid-1] < s[mid] > s[mid+1] :
            return mid
        elif s[mid-1] < s[mid] < s[mid+1] :
            low = mid + 1
        else :
            high = mid -1
    return -1

def solve(n, s) :
    j = binsearch(n, s)
    print(j, s[j])
    
N = int(input())
S = list(map(int, input().split()))
solve(N, S)
