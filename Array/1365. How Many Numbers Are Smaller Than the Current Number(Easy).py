class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {};
        for i, num in enumerate(sorted(nums)):
            count.setdefault(num, i);
        return ([count[num] for num in nums]);

#Record index in sorted nums if it didn't appear before.
#Then just dump it's corresponding index in original nums.
#先排列就能知道某个数前面有多少小于他的