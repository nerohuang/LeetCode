class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0;
        ans = left = 0;
        product = 1;
        for right, num in enumerate(nums):
            product *= num;
            while product >= k:
                product /= nums[left];
                left += 1;
            ans += right - left + 1;
        return ans;

#Our loop invariant is that left is the smallest value so that the product in the 
#window prod = nums[left] * nums[left + 1] * ... * nums[right] is less than k.
#
#For every right, we update left and prod to maintain this invariant. Then, the 
#number of intervals with subarray product less than k and with right-most 
#coordinate right, is right - left + 1. We'll count all of these for each value 
#of right.