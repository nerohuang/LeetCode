class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        j,ss,m = 0,0,l+1

        for i in range(l):
            ss+=nums[i]
            while ss>=s:
                m = min(m, i-j+1)
                ss-=nums[j]
                j+=1
        return m if m<l+1 else 0