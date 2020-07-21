import bisect;

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort();
        ans = 0;
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 1):
                k = bisect.bisect_left(nums, nums[i] + nums[j]);
                ans += max(0, k - 1 - j);
        return ans

#class Solution:
#    def triangleNumber(self, nums: List[int]) -> int:
#        nums.sort()
#        n=len(nums)
#        cnt=0
#        for i in range(n-1,1,-1):
#            ledge=nums[i]
#            l,r=0,i-1
#            while l<r:
#                if nums[l]+nums[r]<=ledge:
#                    l+=1
#                else:
#                    cnt+=r-l
#                    r-=1
#        return cnt