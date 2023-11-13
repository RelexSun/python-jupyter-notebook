def factorize(n, m) :
  if n < 2 :
    return []
  elif m > int(n**0.5) :
    return [n]
  elif n % m == 0 :
    return [m] + factorize(n // m, m)
  else :
    return factorize(n, m + 1)

def solve(n) :
  factors = factorize(n, 2)
  print(" ".join(map(str, factors)))

N = int(input())
solve(N)