class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1;
        while left < right - 1:
            mid = (left + right) // 2;
            if nums[mid] < nums[right]:
                right = mid;
            else:
                left = mid;
        return min(nums[left], nums[right])

# 其实还是个binary search，不用管他怎么转
# 列出三种可能
# [4 5 6 7 1 2 3]
# [1 2 3 4 5 6 7]
# [3 4 5 6 7 1 2]
# 你会发觉，其实就和平时判断binary search没有什么差别。。
# 然后left < right - 1这个right - 1是为了防止死循环
# 然后判断left位置小还是right 位置小就可以了。w