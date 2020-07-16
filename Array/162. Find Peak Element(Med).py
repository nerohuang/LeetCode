class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0;
        if len(nums) == 2:
            return nums.index(max(nums[0], nums[1]));
        for i in range(len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i;
        return len(nums) - 1;

#class Solution:
#    def findPeakElement(self, nums: List[int]) -> int:
#        for i in range(len(nums)):
#            if i > 0 and nums[i] <= nums[i-1]:
#                continue
#            if i < len(nums)-1 and nums[i] <= nums[i+1]:
#                continue
#            return i
#        return 0
#
#class Solution:
#    def findPeakElement(self, nums: List[int]) -> int:
#        left = 0
#        right = len(nums) - 1
#        
#        while left < right:
#            mid = (left + right)//2
#            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
#                return mid
#            elif nums[mid] < nums[mid+1]:
#                left = mid+1
#            else:
#                right = mid-1
#        
#        return left
                