def solve(n, s) :
  stack, operation = [], ""
  j = 0
  x = []
  for i in range(1, n + 1) :
    stack.append(i)
    operation += '+'
    while stack and s[j] == stack[-1] :
      x.append(stack.pop())
      operation += '-'
      j += 1
  print(x)
  return "No" if stack else operation

N = int(input())
S = list(map(int, input().split()))
print(solve(N, S))