# def solve(N) :
#   s = 0
#   for i in range(1, N + 1) :
#     s += i
#   return s


def solve(N):
    return N * (N + 1) // 2


N = int(input(
    "please enter the num:"
))
print(solve(N))
