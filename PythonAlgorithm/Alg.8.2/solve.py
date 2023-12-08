from collections import defaultdict
class HashTable :
    def __init__(self, size) :
        self.size = size
        self.table = defaultdict(list)
    def hash(self, key) :
        return key % self.size
    def get(self, key) :
        return self.table[self.hash(key)]
    def put(self, key, value) :
        self.table[self.hash(key)].append(value)

from HashTable import HashTable

N, M = map(int, input().split())
hashTable = HashTable(M)
for i in range(N) :
    book = input()
    key = sum(map(ord, book))
    hashTable.put(key, book)
for key in range(M) :
    print(key, ", ".join(hashTable,get(key)))
