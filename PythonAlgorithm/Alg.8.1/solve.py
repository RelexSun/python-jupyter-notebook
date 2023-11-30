def hash(s) :
    key = 0
    for i in range(len(s)) :
        key += (ord(s[i]) - ord('a') + 1) * (r ** i)
    return key % M

r, M = map(int, input().split())
S = input()
hashkey = hash(S)
print(hashkey)