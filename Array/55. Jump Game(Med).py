class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxreach = 0
        for i in range(len(nums)):
            if i > maxreach:
                return False
            maxreach = max(maxreach,i+nums[i])
        return True

# 思路
# 这特么是45的简化版。。所以只要45那题有解就能返回true
# 如果走完还没到达最远距离那么就false。