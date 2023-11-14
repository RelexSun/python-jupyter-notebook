def count_factor(n) :
  cnt = 0
  for i in range(2, int(n**0.5) + 1) :
    while n % i == 0 :
      cnt += 1
      n = n // i
  if n != 1 :
    cnt += 1
  return cnt

def solve(n) :
  maxcnt = 0
  for i in range(2, n + 1) :
    maxcnt = max(maxcnt, count_factor(i))
  print(maxcnt)

N = int(input())
solve(N)