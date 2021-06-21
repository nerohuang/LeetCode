class NumArray:

    def __init__(self, nums: List[int]):
        self.curNums = nums.copy()
        self.block = []
        self.width = int(len(nums) ** 0.5)
        for i, num in enumerate(self.curNums):
            if i % self.width == 0:
                self.block.append(num)
            else:
                self.block[-1] += num
                
                
    def update(self, index: int, val: int) -> None:
        i = index // self.width
        diff = val - self.curNums[index]
        self.block[i] += diff
        self.curNums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        i = left // self.width
        j = right // self.width
        ans = sum(self.block[i:j])
        ans += sum(self.curNums[j * self.width : right + 1])
        ans -= sum(self.curNums[i * self.width : left])
        
        return ans


# 思路
# 其实有一个很贱的方法
# 就是用numpy，因为numpy的自我优化问题
# 所以用numpy的array和sum会很快
# 除此之外有一个正常的解法
# 就是用Sqrt Decomposition，这是一个把数组
# 分为每一个长度为sqrt(len(nums))的数组
# 这些数组里面都是这个范围内数字的和
# 所以每次更新数字的时候就要处理一下所属范围的和
# 然后求和的时候，先求出left和right所属的范围
# 然后先加起来，然后再去掉多的和加上少的即可