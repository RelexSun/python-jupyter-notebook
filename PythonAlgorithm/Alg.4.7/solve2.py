def solve(n) :
  cnt = 0
  for a in range(1, n) :
    for b in range(a, n) :
      c = n - a - b
      if b <= c and a + b > c :
        cnt += 1
  return cnt

N = int(input())
print(solve(N))