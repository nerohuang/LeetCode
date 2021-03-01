class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort();
        dp = [[] for _ in range(len(nums))];
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) < len(dp[j]) + 1:
                        dp[i] = dp[j][::];
                        dp[i].append(nums[i]);
            if nums[i] not in dp[i]:
                dp[i].append(nums[i]);
        
        return max(dp, key=len);

# 思路：
# 其实想法是没错的，因为是要找到能整除的数
# 所以先排序，然后建立一个len（nums）长度的DP
# DP用来维护当前位置的数字最多的整除数字，也就是因数。
# 然后先遍历一遍数组，index为i
# 然后再从0遍历到 i - 1 位
# 如果 nums[i] % nums[j] == 0 并且 
# len(dp[i]) < len(dp[j]) + 1
# 那么就在dp[j] 加上nums[i]并赋值到dp[i];
# 如果那个数没有因数，那么dp[i]还是要加上nums[i]
# 因为因数只有他自己。
# 然后返回最长的就行了。