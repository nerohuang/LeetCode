class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        increase = [0 for _ in range(len(nums))];
        decrease = [0 for _ in range(len(nums))];
        increase[0], decrease[0] =1, 1;
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increase[i] = decrease[i - 1] + 1;
                decrease[i] = decrease[i - 1];
            elif nums[i] < nums[i - 1]:
                decrease[i] = increase[i - 1] + 1;
                increase[i] = increase[i - 1];
            else:
                decrease[i] = decrease[i - 1];
                increase[i] = increase[i - 1];
        return max(increase[-1], decrease[-1])

# 思路
# 一个很巧妙的通过维持两个list来计算的dp
# 因为他寻求的是最长的一增一减的子序列
# 所以建立两个list，一个increase，一个decrease
# 分别代表处于增加时index的最长子序列的长度
# 一个是减少是index的最长子序列的长度
# 因为我们可以知道数字只有三种情况：
# 1. nums[i] > nums[i - 1]
# 2. nums[i] < nums[i - 1]
# 3. nums[i] = nums[i - 1]
# 所以应对这三种情况，我们会有三种方式来更新
# list
# 1. 对于第一种， 意思当前的数比前一个数大
# 那么就是增加，这时候要延长有效子序列就是
# 前一个是要减少的，所以我们就
# increase[i] = decrease[i - 1] + 1;
# 而同时因为这次是增加的，那么减少的数列
# 自然不变：
# decrease[i] = decrease[i - 1];
# 2. 对于第二种，情况和第一种类似，就是反过来
# decrease[i] = increase[i - 1] + 1;
# increase[i] = increase[i - 1];
# 3. 对于最后一种，那么不增加不减少，那么
# 两边都继续维持就好了：
# decrease[i] = decrease[i - 1];
# increase[i] = increase[i - 1];
# 然后比较增加和减少序列里面最后一个哪个大
# 就好了。