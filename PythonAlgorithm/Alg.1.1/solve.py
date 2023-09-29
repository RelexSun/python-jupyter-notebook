def madd(A, B) :
    n, m = len(A), len(A[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            C[i][j] = A[i][j] + B[i][j]
    return C

def mprint(A) :
    n, m = len(A), len(A[0])
    for i in range(n) :
        for j in range(m) :
            print(A[i][j], end = " ")
        print()


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = madd(A, B)
mprint(C)

