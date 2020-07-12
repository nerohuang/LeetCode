class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1];
        else:
            length = len(nums);
            return([bisect.bisect_left(nums,target, lo=0, hi=length), bisect.bisect_right(nums,target, lo=0, hi = length) - 1]);

#class Solution:
#    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
#    # array `nums` via binary search.
#    def extreme_insertion_index(self, nums, target, left):
#        lo = 0
#        hi = len(nums)
#        while lo < hi:
#            mid = lo + (hi - lo) // 2
#            if nums[mid] > target or (left and target == nums[mid]):
#                hi = mid
#            else:
#                lo = mid+1
#
#        return lo
#
#
#    def searchRange(self, nums, target):
#        left_idx = self.extreme_insertion_index(nums, target, True)
#
#        if left_idx == len(nums) or nums[left_idx] != target:
#            return [-1, -1]
#
#        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]