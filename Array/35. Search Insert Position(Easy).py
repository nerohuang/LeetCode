class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0;
        right = len(nums) - 1;
        ans = -1;
        while left <= right:
            mid = (left + right) // 2;
            
            if nums[mid] == target:
                return mid;
            
            if target < nums[mid]:
                right = mid - 1;
            
            if target > nums[mid]:
                left = mid + 1;
        
        return left;

# 二分法：
# 一直找，找到就返回
# 找不到，left就刚好会落在他应该插入的地方。
# 可以自己画一个过程看看。