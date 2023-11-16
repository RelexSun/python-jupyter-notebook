def solve(x, low, high) :
    if low >= high :
        print(f"Your x is {low}.")
        return low
    else :
        mid = (low + high) // 2
        print(f"Bigger than {mid}?", end=" ")
        if x > mid :
            print("Yes. ")
            return solve(x, mid + 1, high)
        else :
            print("No. ")
            return solve(x, low, mid)

import random
S, T = map(int, input().split())
SEED = int(input())
random.seed(SEED)
X = random.randint(S, T)
solve(X, S, T)