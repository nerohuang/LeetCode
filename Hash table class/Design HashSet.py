class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        size = 97
        self.size = size
        self.buckets = [list() for i in range(self.size)]
        
    def _hash_num(self, key: int):
        hash_value = key % self.size
        return hash_value

    def add(self, key: int) -> None:
        hash_value = self._hash_num(key)
        self.buckets[hash_value].append(key)

    def remove(self, key: int) -> None:
        hash_value = self._hash_num(key)
        count = 0
        for item in self.buckets[hash_value]:
            if item == key:
                count += 1
        for i in range(count):
            self.buckets[hash_value].remove(key)

    def get(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_value = self._hash_num(key)
        count = 0
        for item in self.buckets[hash_value]:
            if item == key:
                count += 1
        if count > 0:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)