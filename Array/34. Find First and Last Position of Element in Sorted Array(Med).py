class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def binarySearch(nums, target, findLeft):
            left = 0;
            right = len(nums);
            
            while left < right:
                mid = (left + right) // 2;
                if target < nums[mid] or (findLeft and target == nums[mid]):
                    right = mid;
                else:
                    left = mid + 1;
                    
            return left;
        
        leftIndex = binarySearch(nums, target, True);
        
        if leftIndex == len(nums) or nums[leftIndex] != target:
            return [-1, -1];
        
        return [leftIndex, binarySearch(nums, target, False)-1]

# 思路：
# 一样是二分法，不过这是个变形
# 情况就是我们要找到一左一右
# 我们首先要找到最左边的：
# 思路和一般的二分法差不多，不过是当 nums[mid] == traget
# 的时候，我们同样要把mid = right， 这样的话我们就能假设
# right的位置已经是在一串或一个target里面
# 这时候继续二分法找，如果还找到一样的，说明不是最左边那个target
# 那么继续 mid = target，直到left == right
# 返回left就是最左边的target了。
# 然后找最右边的target：
# 其实就是找第一个大于target的数字
# 所以除非 target < nums[right]， left会一直等于mid + 1；
# 直到left == right
# 这个时候就会是大于target的第一个数字
# 然后返回left并且把结果-1就是最右边的target