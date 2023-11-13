def is_palindrome(n) :
    s = str(n) 
    r = s[::-1] 
    return int(s) == int(r)

def solve(n, m) :
    cnt = 0
    for i in range(n, m + 1) :
        if is_palindrome(i) :
            cnt += 1
    return cnt

N, M = map(int, input().split())
print(solve(N, M))