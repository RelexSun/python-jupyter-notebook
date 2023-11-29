from heappq import heappush, heappop

def solve(cmd, heap) :
    if cmd[0] == "push" :
        heappush(heap, int(cmd[0]))
    elif cmd[0] == "pop" :
        print(0 if not heap else heappop(heap))
    print(cmd, heap)

N = int(input())
heap = []
for _ in range(N) :
    cmd = input().split()
    solve(cmd, heap)