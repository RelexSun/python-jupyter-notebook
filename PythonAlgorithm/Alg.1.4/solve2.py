import time
N = int(input('enter an integer: '))
while N < 0 :
    N = int(input('Enter positive number: '))

start = time.time()


def solve2(n) :
    a = int(n**0.5)
    cnt = 0
    for i in range(1, a + 1) :
        if n % i == 0 :
            cnt += 2
        elif a * a == n :
            cnt -= 1
    return cnt

print(solve2(N))

end = time.time()

print("solve() elapsed time: {}".format(end - start))