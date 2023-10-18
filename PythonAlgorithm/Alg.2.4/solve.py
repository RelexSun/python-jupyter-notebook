def hanoi(n, src, via, dst) :
  global cnt
  if n == 1 :
    cnt += 1
    # print(f"{src} -> {dst}")
  else :
    hanoi(n - 1, src, dst, via)
    hanoi(1, src, via, dst)
    hanoi(n - 1, via, src, dst)

N = int(input())
cnt = 0
hanoi(N, "A", "B", "C")
print(cnt)