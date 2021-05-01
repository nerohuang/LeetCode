class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort();
        
        goal = sum(nums)//2;
        if sum(nums)%2 == 1:
            return False;
        
        dp = [False for _ in range(goal + 1)];
        
        dp[0] = True;
        
        for num in nums:
            for i in range(goal, num - 1, -1):
                dp[i] = dp[i] or dp[i - num];
        
        return dp[goal]

# 这题有两个做法，先说dp
# 因为我们要找到两个subset是相等的，所以我们首先找到这个数组
# 的和的一半，如果求余等于1，那么就说明该数列的和不能被分为两半
# 返回false， 如果是0，则返回true，并称之为goal；
# 然后建一个长度为goal + 1的数组，初始值都为False，代表在0和goal
# 之间的数字是否和subset的和相等。
# 然后两个for loop，一个遍历所有的num，第二层就是从goal 反过来遍历刀
# num；
# 然后如果 dp[i-num]是True的话，那么dp[i]也是true，因为这样表示
# 表示dp[i - num] + num 能得到 i，而之前[i-num]也有组合能组成，那么
# 能传递下去。然后返回dp[goal]看看是T还是F，如果是T那么表示有组合能组成
# goal，反之亦然。
# 为什么要从goal倒过来到num是因为防止如果num第一个是1，那么就会使dp[1]变成true
# 然后dp[2]也变成true，一直下来DP就失效了。

# 另一个做法是DFS
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/950822/Python-3-Solution-Explained-(video-%2B-code)