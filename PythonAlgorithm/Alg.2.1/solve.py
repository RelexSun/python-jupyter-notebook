import sys

sys.setrecursionlimit(10**6)
# without the setrecursionlimit the limit will be 1000 by default.
# We can modify this through the code above.

def fact(n) :
    if n == 0 :
        return 1
    return n * fact(n-1)
    
x = int(input())    
print(fact(x))
