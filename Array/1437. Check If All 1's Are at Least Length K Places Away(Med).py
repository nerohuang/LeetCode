class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True;
        
        try:
            mark = nums.index(1);
        except:
            return True
        if mark + 1 >= len(nums):
            return True;
        for i in range(mark + 1, len(nums)):
            if nums[i] == 1:
                if i - mark - 1 < k:
                    return False;
                mark = i;
        return True
                