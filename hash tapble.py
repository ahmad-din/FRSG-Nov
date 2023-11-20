class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

# Example usage:
hash_table = HashTable()

hash_table.insert(120, "apple")
hash_table.insert(80, 'dragon frout')
hash_table.insert(90, 'peach')
hash_table.insert(432, "mango")
hash_table.insert(211, "banana")
hash_table.insert(543, "orange")  # Collision with index 3
hash_table.insert(753, "grape")   # Collision with index 3

print("Search 213:", hash_table.search(213))  # Output: Search 213: banana
print("Search 543:", hash_table.search(543))  # Output: Search 543: orange

hash_table.delete(432)
print("After removal:", hash_table.table)
