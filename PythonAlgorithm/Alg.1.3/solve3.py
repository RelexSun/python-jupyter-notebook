def solve(n, s) :
  maxn, maxi = s[0], 0
  for i in range(1, n) :
    if maxn < s[i] :
      maxn, maxi = s[i], i
  return maxn, maxi

N = int(input())
S = list(map(int, input().split()))
maxn, maxi = solve(N, S)
print(maxn, maxi)