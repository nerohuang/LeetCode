class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0;
        total = 0;
        
        for num in nums:
            total += num;
            min_sum = min(min_sum, total);
        
        return max(1, 1 - min_sum)


#import itertools
#class Solution:
#    def minStartValue(self, nums: List[int]) -> int:
#        return (1-min(accumulate(nums, initial = 0)))