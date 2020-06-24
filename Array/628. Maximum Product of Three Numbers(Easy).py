class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort();
        prodcut1 = nums[-1] * nums[-2] * nums[-3];
        product2 = nums[0] * nums[1] * nums[-1];
        return prodcut1 if prodcut1 > product2 else product2


##class Solution:
##    def maximumProduct(self, nums: List[int]) -> int:
##        nums.sort()
##        r = reduce(lambda a,b: a*b, nums[-3:], 1)
##        r0 = reduce(lambda a,b: a*b, nums[:2] + [nums[-1]], 1)
##        return max(r,r0)