class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        nums = [float("inf")] + nums + [float("inf")];
        ans = [0 ,0];
        for i in range(1, len(nums) - 1):
            ans[i % 2] += max(0, nums[i] - min(nums[i + 1], nums[i - 1]) + 1)
        return min(ans)

#思路就是三个三个一组，然后每一组假设都符合： A[i - 1] > A[i] < A[i + 1];
#这样的话可以得出每一个偶数位和奇数位，并找出每一个中位需要加/减多少并根据奇偶位求和
#最后返回要求少的那个
#
#One pass, making each element local minimum.
#
#[9,6,1,6,2]
#i = 0, [inf, 9, 6], 9 => 5, even cost 4
#i = 1, [9, 6, 1], 6 => 0, odd cost 6
#i = 2, [6, 1, 6], 1 => 1, even cost 0
#i = 3, [1, 6, 2], 6 => 0, odd cost 12
#i = 4, [6, 2, inf], 2 => 2, even cost 0
#total even cost 4, new array => [5, 6, 1, 6, 2]
#total odd cost 18, new array => [9, 0, 1, 0, 2]
#
#find the min(A[i - 1],A[i + 1]),
#calculate that the moves need to make smaller than both side.
#If it's negative, it means it's already smaller than both side, no moved needed.
#Add the moves need to res[i%i].
#In the end return the smaller option.