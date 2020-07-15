class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        if target not in nums:
            return -1;
        
        maxNum = max(nums);
        maxNumIndex = nums.index(maxNum);
        if target == maxNum:
            return maxNumIndex;
        if target > maxNum:
            return -1;
        if target >= nums[0]:
            return bisect.bisect_left(nums,target, lo=0, hi=maxNumIndex);
        if target < nums[0]:
            return bisect.bisect_left(nums,target, lo=maxNumIndex + 1, hi=len(nums));

#class Solution:
#    def search(self, nums: List[int], target: int) -> int:
#        left = 0
#        right = len(nums)-1
#        
#        while(left<=right):
#            
#            mid = (left+right)//2
#            
#            if nums[mid] == target:
#                return mid
#            
#            elif nums[left] <= nums[mid]:
#                if nums[left] <= target and target < nums[mid]:
#                    right = mid - 1 
#                else:
#                    left = mid + 1
#                
#            elif nums[left] > nums[mid]:
#                if nums[right] >= target and nums[mid] < target:
#                    left = mid + 1
#                else:
#                    right = mid - 1
#        
#        return -1