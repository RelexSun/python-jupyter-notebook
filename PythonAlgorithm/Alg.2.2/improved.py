def gcd(n, m) :
  while m != 0 :
    n, m = m, n % m
  return n
  
N = int(input())
M = int(input())

print(gcd(N, M))
