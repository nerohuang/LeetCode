class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        s = list(reversed(sorted(nums)))
        try:
            if s[0] >= s[1]*2:
                return nums.index(s[0])
            else:
                return -1
        except:return -1