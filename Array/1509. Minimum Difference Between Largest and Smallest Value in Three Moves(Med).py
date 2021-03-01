class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0;
        nums.sort();
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])

#思路
#这有个很奇妙的逻辑
#首先如果这数组小于等于4个的时候，就能改变任意三个
#所以差值永远为0
#当大于4个的时候，最理想的当然是改变最大的或者最小的
#我们先排个序得到
#[0,1,2,3, ...... ,i-3, i-2, i-1, i]
#因为改三个，所以可以：
#改变0，1，2变成3的数值
#改变0，1变成2的数值，i变成i-1的数值
#改变0变成1的数值，i-1, i变成i-2的数值
#改变i-2,i-1,i变成i-3的数值
#所以其实就是比较
#nums[i] - nums[3]
#nums[i - 1] - nums[2]
#nums[i - 2] - nums[1]
#nums[i - 3] - nums[0];
#这四种情况。