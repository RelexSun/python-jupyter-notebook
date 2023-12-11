def solve(n) :
  T = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

  roman = ""
  for num, val in T.items() :
    while n >= num :
      roman += val
      n -= num
  return roman

N = int(input())
print(solve(N))

