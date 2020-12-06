class NumArray:

    def __init__(self, nums: List[int]):
        if not nums: return 
        self.store =[0 for _ in range(len(nums))];
        
        self.store[0] = nums[0];
        for i in range(1, len(nums)):
            self.store[i] = self.store[i - 1] + nums[i];

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.store[j];
        else:
            return self.store[j] - self.store[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)