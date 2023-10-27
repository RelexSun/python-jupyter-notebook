s = [(2, 5), (2, 1), (1, 3), (1, 4), (1, 2)]

# print(sorted(s, key = lambda k: k[0]))
# print(sorted(s, key = lambda k: k[1]))

print(sorted(s, key = lambda k: (k[0], k[1])))

print(sorted(s, key = lambda k: (k[0], -k[1])))

s.sort(key = lambda k: (k[0], -k[1]))
print(s)