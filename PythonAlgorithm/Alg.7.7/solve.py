def solve(n, k, m) :
    queue = [i for i in range(1, n + 1)]
    j, r = 0, 0
    while queue :
        if (r // m) % 2 == 0 :
            j = (j + k - 1) % len (queue)
        else :
            j = (j - k) % len(queue)
        r += 1
        print(queue.pop(j), end = " ")
    print()

N, K, M = map(int, input().split())
solve(N, K, M)