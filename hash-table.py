class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)] 

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return(f"Key {key} not found")

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        return(f"Key {key} not found")

# Example on how to use it

ht = HashTable(size=5)
ht.insert("name", "Maria")
ht.insert("age", 25)
ht.insert("city", "Sao Paulo")
ht.insert("name", "Carlos")  
print(f"Hash Table: {ht}")
print(f"Get 'name': {ht.get('name')}")  
print(f"Get 'city': {ht.get('city')}") 
ht.remove("age")
print(f"Hash Table after removing 'age': {ht}")