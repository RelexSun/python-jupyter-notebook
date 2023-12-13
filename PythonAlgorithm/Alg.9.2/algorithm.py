
def solve(n, A, B) :
    print("A+B:")
    mprint(n, madd(n, A, B))
    print("A*B:")
    mprint(n, mmult(n, A, B))

def madd(n, A, B) :
    C = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            C[i][j] = A[i][j] + B[i][j]
    return C

def mmult(n, A, B) :
    C = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            for k in range(n) :
                C[i][j] += A[i][k] * B[k][j]
    return C

def mprint(n, A) :
    for i in range(n) :
        print(*A[i])

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
solve(N, A, B)