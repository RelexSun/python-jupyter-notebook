def solve(x, s, t) :
    low, high = s, t
    while low < high :
        mid = (low + high) // 2
        print(f"Bigger than {mid}?", end=" ")
        if x > mid :
            print("Yes. ")
            low = mid + 1
        else :
            print("No. ")
            high = mid
    print(f"Your x is {low}.")
    return low

import random
S, T = map(int, input().split())
SEED = int(input())
random.seed(SEED)
X = random.randint(S, T)
solve(X, S, T)