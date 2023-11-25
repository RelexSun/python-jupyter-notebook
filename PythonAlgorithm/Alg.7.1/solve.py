def solve(cmd, queue) :
    if cmd[0] == 'enqueue' :
        queue.append(cmd[1])
    elif cmd[0] == 'dequeue' :
        print('Oops!' if len(queue) == 0 else queue.pop(0))
    elif cmd[0] == 'peek' :
        print("None!" if len(queue) == 0 else queue[0])
    elif cmd[0] == 'size' :
        print(len(queue))
    elif cmd[0] == 'empty' :
        print(len(queue) == 0)
        
# Accept the number of commands as an int input
N = int(input()) 

# Initialize the queue as an empty list since we need to use it with queue operations.
queue = []

# The sovle function receives cmd and the queue to solve the respective problem, 
# so it takes cmd as input for the number of commands
for _ in range(N) :
    cmd = input().split() # The input string is divided using the 'split' and assigned to cmd.
    solve(cmd, queue) 