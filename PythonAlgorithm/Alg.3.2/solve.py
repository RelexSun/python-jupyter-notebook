s = [(3, 5), (2, 1), (5, 3), (1, 4), (4, 2)]

# will sort in ascending order 
# [(1, 4), (2, 1), (3, 5), (4, 2), (5, 3)]
# def first(k) :
#   return k[0]

# print(sorted(s, key = first))
# print(sorted(s, key = second, reverse = True))

# will sort in descending order 
# [(2, 1), (4, 2), (5, 3), (1, 4), (3, 5)]
def second(k) :
  return k[1]

print(sorted(s, key = second))
# print(sorted(s, key = first, reverse = True))