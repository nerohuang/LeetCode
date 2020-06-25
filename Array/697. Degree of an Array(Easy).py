class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {};
        for num in nums:
            count[num] = count.get(num, 0) + 1;
        
        ans = len(nums);
        degree = max(count.values());
        for num in count:
            if count[num] == degree:
                ans = min(ans, len(nums) - nums[::-1].index(num) - 1 - nums.index(num) + 1);
        return ans;



##class Solution:
##    def findShortestSubArray(self, nums: List[int]) -> int:
##        left, right, count = {}, {}, {};
##        for i, num in enumerate(nums):
##            if num not in left:
##                left[num] = i;
##            right[num] = i;
##            count[num] = count.get(num, 0) + 1;
##        
##        ans = len(nums);
##        degree = max(count.values());
##        for num in count:
##            if count[num] == degree:
##                ans = min(ans, right[num] - left[num] + 1);
##        return ans;

##class Solution:
##    def findShortestSubArray(self, nums: List[int]) -> int:
##        freq = collections.Counter(nums)
##        degree = max(freq.values())
##        if degree == 1:
##            return 1
##        
##        res = float('inf')
##        candidates = [n for n in freq if freq[n] == degree]
##        for candidate in candidates:
##            l = nums.index(candidate)
##            r = len(nums) - nums[::-1].index(candidate)
##            res = min(res, r-l)
##            
##        return res