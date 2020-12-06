class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        store = [nums[0]];
        store.append(max(nums[0], nums[1]));
        for i in range(2, len(nums)):
            store.append(max(store[i - 1], nums[i] + store[i - 2]));
        
        return store[-1]

#思路：
#先建立一个list dp，然后dp[i]就是[0,i]之间可以抢到的最大值；
#对于当前i来说，有抢和不抢两种选择：
#如果不抢，那么就是dp[i-1]（等价于去掉 nums[i] 只抢 [0, i-1] 区间最大值）
#如果抢，就是nums[i] + dp[i-2]，因为不能抢相邻的，等价于去掉nums[i-1]
#然后一直遍历到最后一位就能知道最大得益是多少。

#比如说 nums为{3, 2, 1, 5}，那么来看 dp 数组应该是什么样的，首先 dp[0]=3 
#没啥疑问，再看 dp[1] 是多少呢，由于3比2大，所以抢第一个房子的3，当前房子
#的2不抢，则dp[1]=3，那么再来看 dp[2]，由于不能抢相邻的，所以可以用再前面
#的一个的 dp 值加上当前的房间值，和当前房间的前面一个 dp 值比较，取较大值
#当做当前 dp 值，这样就可以得到状态转移方程 
#dp[i] = max(num[i] + dp[i - 2], dp[i - 1]), 
#且需要初始化 dp[0] 和 dp[1]，其中 dp[0] 即为 num[0]，
#dp[1] 此时应该为 max(num[0], num[1])