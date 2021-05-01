class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -999999999999999999999999999999999;
        curSum = 0;
        store = [];
        for num in nums:
            store.append(num);
            curSum = sum(store);
            if num > curSum:
                store = [];
                store.append(num);
                curSum = num;
            if maxSum < curSum:
                maxSum = curSum;
        return maxSum;

#class Solution:
#    def maxSubArray(self, nums: List[int]) -> int:
#        # Initialize our variables using the first element.
#        current_subarray = max_subarray = nums[0]
#        
#        # Start with the 2nd element since we already used the first one.
#        for num in nums[1:]:
#            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
#            current_subarray = max(num, current_subarray + num)
#            max_subarray = max(max_subarray, current_subarray)
#        
#        return max_subarray

# 思路： 其实可以用DP来做
# 如果当前的数字num比curSum+num大，那就curSum就变成num，如果不是就累加
# 然后对比maxSum 