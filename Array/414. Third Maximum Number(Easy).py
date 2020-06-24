class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums);
        nums_list = list(nums_set)
        nums_list.sort();
        if len(nums_list) >= 3:
            return nums_list[-3];
        else:
            return nums_list[len(nums_list) - 1]

##class Solution:
##    def thirdMax(self, nums: List[int]) -> int:
##        
##        nums = set(nums)
##        
##        maximum = max(nums)
##        
##        if len(nums) < 3:
##            return maximum
##        
##        nums.remove(maximum)
##        second_max = max(nums)
##        nums.remove(second_max)
##        return max(nums)