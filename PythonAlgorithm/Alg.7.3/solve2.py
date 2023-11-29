from heapq import heappush, heappop

def solve(cmd, heap) :
    if cmd[0] == "push" :
        x = int(cmd[1])
        heappush(heap, (abs(x),x))
    elif cmd[0] == "pop" :
        print(0 if not heap else heappop(heap)[1])
    print(cmd, heap)

N = int(input())
heap = []
for _ in range(N) :
    cmd = input().split()
    solve(cmd, heap)