class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        size = 97
        self.size = size
        self.buckets = [None] * size
        
    def _hash_num(self, key: int):
        hash_value = key % self.size
        return hash_value

    def put(self, key: int, value: int) -> None:
        hash_value = self._hash_num(key)
        if not self.buckets[hash_value]:    
            self.buckets[hash_value] = [[key, value]]
            return
        
        for i in range(len(self.buckets[hash_value])):
            if self.buckets[hash_value][i][0] == key:
                self.buckets[hash_value][i][1] = value
                return
        self.buckets[hash_value].append([key, value])

    def remove(self, key: int) -> None:
        hash_value = self._hash_num(key)
        if self.buckets[hash_value]:
            for i in range(len(self.buckets[hash_value])):
                if self.buckets[hash_value][i][0] == key:
                    del self.buckets[hash_value][i]
                    break
            if len(self.buckets[hash_value]) == 0:
                self.buckets[hash_value] =  None

    def get(self, key: int) -> int:
        """
        Returns true if this set contains the specified element
        """
        hash_value = self._hash_num(key)
        if self.buckets[hash_value]:
            for item in self.buckets[hash_value]:
                if item[0] == key:
                    return item[1]
        
        return -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)