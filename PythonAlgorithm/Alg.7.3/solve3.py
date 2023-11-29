from heapq import heappush, heappop

def solve(cmd, heap) :
    if cmd[0] == "push" :
        heappush(heap, -int(cmd[1]))
    elif cmd[0] == "pop" :
        print(0 if not heap else -heappop(heap))

N = int(input())
heap = []
for _ in range(N) :
    cmd = input().split()
    solve(cmd, heap)