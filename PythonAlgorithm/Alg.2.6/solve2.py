def fib(n) :
    if n == 1 or n == 2 :
        return 1
    else :
        a, b = 1, 1
        for _ in range(3, n + 1) :
            a, b = b, a + b
        return b
N = int(input())
print(fib(N))