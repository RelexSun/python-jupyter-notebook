def gcd(n, m) :
  print(n, m)
  if m == 0 :
    return n
  else :
    return gcd(m, n % m)
  
N = int(input())
M = int(input())

print(gcd(N, M))