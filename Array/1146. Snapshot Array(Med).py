class SnapshotArray:
    
    

    def __init__(self, length: int):
        self.arr = {};
        self.snapstore = [];

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val;

    def snap(self) -> int:
        self.store = self.arr.copy();
        self.snapstore.append(self.store);
        return len(self.snapstore) - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snapstore[snap_id]:
            return self.snapstore[snap_id][index];
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

#用dict代替数组，index就作为key