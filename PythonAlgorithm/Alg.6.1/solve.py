def solve(cmd, stack) :
    if cmd[0] == "push" :
        stack.append(cmd[1])
    elif cmd[0] == "pop" :
        print("Oops!" if len(stack) == 0 else stack.pop())
    elif cmd[0] == "peek" :
        print("None!" if len(stack) == 0 else stack[-1])
    elif cmd[0] == "size" :
        print(len(stack))
    elif cmd[0] == "empty" :
        print(len(stack) == 0)
        
N = int(input())
stack = []
for _ in range(N) :
    cmd = input().split()
    solve(cmd, stack)