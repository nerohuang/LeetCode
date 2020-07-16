class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0;
        right = len(nums) - 1;
        

        
        while (left <= right):
            if right - left == 0:
                return nums[0];
            if right - left == 1:
                return min(nums[left], nums[right]);
            
            mid = (left + right) // 2;
            
            if nums[mid] < nums[mid + 1] and nums[mid - 1] > nums[mid]:
                return nums[mid];
            
            if nums[left] < nums[mid] and nums[mid] < nums[right]:
                right = mid;
            elif nums[mid] < nums[left] and nums[mid] < nums[right]:
                right = mid;
            elif nums[left] < nums[mid] and nums[right] < nums[mid]:
                left = mid;

#class Solution:
#    def findMin(self, nums: List[int]) -> int:
#        i = 0
#        j = len(nums) - 1
#        while i < j-1:
#            m = (j+i) // 2
#            if nums[m] < nums[j]:
#                j = m
#            else:
#                i = m 
#
#        return min(nums[i], nums[j])