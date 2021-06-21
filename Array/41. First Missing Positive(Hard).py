class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numRecords = [False] * (len(nums) + 1);
        
        for num in nums:
            if 0 < num <= len(nums):
                numRecords[num] = True
        
        for i in range(1, len(numRecords)):
            if not numRecords[i]:
                return i
        
        if not numRecords:
            return 1
        return len(nums) + 1

# 思路：
# 有点脑筋急转弯
# 整体思路是新建一个长度为len(nums) + 1的，初始值都为false
# 的数组，然后遍历第一遍nums，如果里面的元素大于0小于len（nums）
# 那么就在records里面标记为True，此时为O（n）
# 开始遍历第二次，从1开始遍历records，如果其中有false，那么表明那个
# nums的数组里面没有这个正数，返回即可，并且因为是按顺序从小到大
# 遍历
# 当遍历完没找到的话，说明缺失的最小正数那只能是len(nums) + 1了
# 因为len(nums)里面的正数都被nums包圆了