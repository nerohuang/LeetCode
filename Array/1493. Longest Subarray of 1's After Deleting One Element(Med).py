class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1;
        i, j = 0, 1;
        ans = 0;
        count = 1;
        flag = False;
        zeroMark = 0;
        countZero = 0;
        for k in range(len(nums)):
            if nums[k] == 0:
                countZero += 1;
            else:
                break;
        nums = nums[countZero:];
        
        while i <= j and j < len(nums):
            if nums[j]:
                count += 1;
                ans = max(ans, count);
                j += 1;
            else:
                if not flag:
                    zeroMark = j;
                    ans = max(ans, count);
                    flag = True;
                    j += 1;
                else:
                    count -= zeroMark - i;
                    i = zeroMark + 1;
                    flag = False;
        return ans; 