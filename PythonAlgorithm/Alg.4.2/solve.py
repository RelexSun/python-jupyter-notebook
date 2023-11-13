def is_palindrome(n):
    r, m = 0, n
    while m > 0:
        r *= 10
        r += m % 10
        m //= 10
    return n == r


def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        if is_palindrome(i):
            cnt += 1
            print(i)
    return cnt


N, M = map(int, input().split())
print(solve(N, M))
