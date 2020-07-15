class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True;
        lastPostion = len(nums) - 1;
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPostion:
                lastPostion = i;
        return True if lastPostion == 0 else False;

#class Solution:
#    def canJump(self, nums: List[int]) -> bool:
#        
#        maxreach = 0
#        for i in range(len(nums)):
#            if i > maxreach:
#                return False
#            maxreach = max(maxreach,i+nums[i])
#        return True