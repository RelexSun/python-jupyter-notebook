def solve2(n, s) :
    stack = []
    for i in range(n) :
        while len(stack) > 0 and s[i] >= stack[-1] :
            stack.pop()
        stack.append(s[i])
    return len(stack)

N = int(input())
S = list(map(int, input().split()))
print(solve2(N, S))