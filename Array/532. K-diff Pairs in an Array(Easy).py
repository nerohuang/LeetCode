class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        i, j = 0, 1;
        nums.sort();
        pair = set();
        while i < j and j < len(nums):
            if nums[j] - nums[i] == k:
                pair.add((nums[j], nums[i]));
                i += 1;
                j = i + 1;
            elif nums[j] - nums[i] > k:
                i += 1;
                j = i + 1;
            else:
                j = j + 1;
        return len(pair);

##class Solution:
##    def findPairs(self, nums: List[int], k: int) -> int:
##        if k < 0:
            return 0
##        
##        import collections
##        hm = collections.Counter(nums)
##        
##        result = 0
##        if k == 0:
            for i in hm:
                if hm[i] > 1:
                    result += 1
##        else:
            for i in hm:
                if (i - k) in hm.keys():
                    result += 1
##        return result