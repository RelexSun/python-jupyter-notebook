def solve(S) :
    opening = "[{("
    closing = "]})"
    stack = []
    for s in S :
        if s in opening :
            stack.append(s)
        elif stack and opening.index(stack[-1]) == closing.index(s) :
            stack.pop()
        else :
            return False 
    return len(stack) == 0

S = input()
print("Yes" if solve(S) else "No")