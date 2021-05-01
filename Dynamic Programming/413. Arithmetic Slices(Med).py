class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0;
        dp = [0 for _ in range(len(nums))];
        for i in range(2, len(nums)):
            if nums[i - 2] - nums[i - 1] == nums[i - 1] - nums[i]:
                dp[i] = dp[i - 1] + 1;
        return sum(dp)

# 思路，dp
# 情况是这样，他说要等差数列，所以一个合格的等差切片
# 最少要三个元素，那么就能得到等式：
# nums[i - 2] - nums[i - 1] == nums[i - 1] - nums[i]
# 然后我们可以从2开始遍历到最后来来看看有多少组切片是符合规定的
# 但是等差数列不止3个元素啊，那么怎么办？
# 其实这个等式有个连贯性，比如：
# [1,2,3,4]
# [2,3,4] [1,2,3,4]
# 当i在3的时候能得出 
# [1,2,3] 
# 那么i在4的时候能得出
# [2,3,4]，但是因为1-2=2-3=3-4
# 所以这样也能组成一个等差数列
# 所以就是dp[i-1] + 1 = dp[i]
# 然后最后sum(dp)就能得出所有等差数列的个数了。