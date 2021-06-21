class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        
        cur = 1
        answer = 0
        
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                cur += 1
            else:
                answer = max(cur, answer)
                cur = 1
            
        return max(answer, cur)

# 很简单得一道题，但他要求时长是O(n)
# 排序了好像就是nlogn
# 好像有其他做法
# class Solution:
#   def longestConsecutive(self, nums):
#       longest_streak = 0
#       num_set = set(nums)
#
#       for num in num_set:
#           if num - 1 not in num_set:
#               current_num = num
#               current_streak = 1
#
#               while current_num + 1 in num_set:
#                   current_num += 1
#                   current_streak += 1
#
#               longest_streak = max(longest_streak, current_streak)
#
#       return longest_streak

# 这个就是不排序的，是O(2n)所以就是O（n）
# 有点莫名其妙