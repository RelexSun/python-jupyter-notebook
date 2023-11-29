def solve(cmd, queue: deque) :
  if cmd[0] == 'push_front' :
    queue.append(cmd[1])
  elif cmd[0] == "push_back" :
    queue.appendleft(cmd[1])
  elif cmd[0] == "pop_front" :
    print("Oops!" if not queue else queue.pop())
  elif cmd[0] == 'pop_back' :
    print("Oops!" if not queue else queue.popleft())
  elif cmd[0] == 'peek_front' :
    print("None!" if not queue else queue[-1])
  elif cmd[0] == 'peek_back' :
    print("None!" if not queue else queue[0])

from collections import deque
N = int(input())
queue = deque()
for _ in range(N) :
  cmd = input().split()
  solve(cmd, queue)