class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target not in nums:
            return False;
        
        maxNum = max(nums);
        maxNumIndex = nums.index(maxNum);
        if target == maxNum:
            return True;
        if target > maxNum:
            return False;
        if target >= nums[0]:
            if bisect.bisect_left(nums,target, lo=0, hi=maxNumIndex) == -1:
                return False
            else:
                return True
        if target < nums[0]:
            if bisect.bisect_left(nums,target, lo=maxNumIndex + 1, hi=len(nums)) == -1:
                return False
            else:
                return True


#class Solution:
#    def search(self, nums: List[int], target: int) -> bool:
#        left, right = 0, len(nums) - 1
#        while left <= right:
#            mid = (left + right) // 2
#            # if found target value, return the index
#            if nums[mid] == target:
#                return True
#            if nums[left] == nums[mid] and nums[mid] == nums[right]:
#                left += 1
#                right -= 1
#            elif nums[mid] >= nums[left]: # left rotated
#                # in ascending order side
#                if nums[left] <= target and target < nums[mid]:
#                    right = mid - 1
#                else:
#                    left = mid + 1
#            else: # right rotated
#                # in ascending order side
#                if nums[mid] < target and target <= nums[right]:
#                    left = mid + 1
#                else:
#                    right = mid - 1
#        # cannot find the target value
#        return False