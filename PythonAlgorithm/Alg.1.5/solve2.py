import time

def solve(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())

start = time.time()
print("YES" if solve(N) else "NO")
end = time.time()
print(end - start)