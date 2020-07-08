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
#        max_sum, curr_sum = -math.inf, 0
#        
#        for num in nums:
#            curr_sum += num
#            max_sum = max(max_sum, num, curr_sum)
#            if curr_sum < 0:
#                curr_sum = 0
#                
#        return max_sum