def solve(n, p) :
    p.sort(key = lambda x: (x[0], -x[1]))
    for i in range(n) :
        print(" ".join(map(str, p[i])))
        
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
solve(N, P)