def solve(n):
    cnt = 0

# The size of the input can be denoted as 'n', and from 1 to n, the basic operation involves checking whether the remainder of dividing n by i is 0.
# It can be understood that this operation is performed a total of n times.
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return (cnt)

N = int(input())
import time 
start = time.time()

print(solve(N))

end = time.time()

print("solve() elapsed time: {}".format(end - start))

# --------------------------------------------------------------
# print(len([i for i in range(1, N + 1) if N % i == 0]))
# --------------------------------------------------------------
# div = list(x for x in map(lambda x : 8 % x == 0, range(1, 9)) if x )
# print(len(div))
