def solve(x) :
    stack = []
    for x in X :
        if x.isdigit() :
            stack.append(int(x))
        else :
            b, a = stack.pop(), stack.pop()
            if x == '+' : stack.append(a+b) 
            elif x == '-' : stack.append(a-b)
            elif x == '*' : stack.append(a*b)
            elif x == '/' : stack.append(a//b)
        print(stack)
    return stack[-1]

X = input()
print(X)
print(solve(X))        