class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0;
        if len(nums) <= 3:
            return max(nums);
        
        def calulate(dp):
            store = [dp[0]];
            store.append(max(dp[0], dp[1]));
            
            for i in range(2, len(dp)):
                store.append(max(store[i - 1], dp[i] + store[i - 2]));
            
            return store[-1];
        
        p1 = calulate(nums[:len(nums) - 1]);
        p2 = calulate(nums[1:]);
        
        return max(p1, p2)
            
#思路和上一题其实是一样得
#但因为是闭环，所以就变成了寻找 1 到 N-1 和 2 到 N 之间的最大值。
#所以做两遍，然后找出最大值。
