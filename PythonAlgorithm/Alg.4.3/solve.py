import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return int(s) == int(r)


def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        if is_palindrome(i) and is_prime(i) : 

## runtime really depends on which one you checked for first

            cnt += 1
            print(i)
    return cnt


N, M = map(int, input().split())

start = time.time()
print(solve(N, M))
end = time.time()
print(f"solve() elapsed time = {end - start}")
