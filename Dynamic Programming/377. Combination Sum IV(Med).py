class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = [0];
        
        def findSum(target):
            for num in nums:
                if target - num > 0:
                    findSum(target - num);
                if target - num == 0:
                    ans[0] += 1;
            return
        findSum(target);
        return ans[0]

# 超时了！ dp！

#class Solution:
#    def combinationSum4(self, nums: List[int], target: int) -> int:
#        ## RC ## 
#        ## APPROACH : DP ##
#        # 1. Base case : Number of combinations to make 0 is 0.
#        # 2. consider nums= {1,2,3}
#        # 3. target = 1, combinations = {1}
#        # 4. target = 2, combinations = {1,1}, {2}
#        # 5. target = 3, combinations = {1,1,1} , {1,2}, {2,1}, {3}
#        # 6. If number is in the list, you can directly count it as one combination
#        # 7. else include all the combinations of target - nums[i]
#        
#		## TIME COMPLEXITY : O(N^2) ##
#		## SPACE COMPLEXITY : O(N) ##
#
#        dp = [0] * (target+1) 
#        for i in range(1, target+1):            # offset from 1 to skip base case (first element)
#            for n in nums:
#                if( n == i):                    # If number is in the list, you can directly count it as one combination
#                        dp[i] += 1
#                if n < i:                       
#                        dp[i] += dp[i-n]        # include all the combinations of target i-n.
#        return dp[-1]

# 其实是一个十分简单的dp。。
# 创建一个target+1长度的list
# 然后从1遍历到target，然后每到一个数字
# 就遍历一遍给出的数组。
# 如果数组里面数字n等于dp的数字i，那么就直接dp[i] + 1
# 如果数字n小于i，那么dp[i] = dp[i] + dp[i - n];
