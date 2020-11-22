class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0;
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        ans += 1;
        return ans


#rating = [2,5,3,4,1];
#
#n = len(rating)
#dp_g, dp_l = [0] * n, [0] * n
#res = 0
#for i, r in enumerate(rating):
#    for j in range(i):
#        if r > rating[j]:
#            dp_g[i] += 1
#            res += dp_g[j]
#        elif r < rating[j]:
#            dp_l[i] += 1
#            res += dp_l[j]
#
#print(res)

#找数组中长度为3的递增序列和递减序列的总数。increasing subseq => DP。
#当遍历到i时，nums[i]会作为序列尾（第三个元素），需要对前面的j的已有结果，
#也就是序列长度为2的，做遍历，因此dp[j]存以nums[j]为递增（减）序列第二个
#位置时序列的个数。i每次能和前面j拼在一起时，res += dp[j]。

#动态规划：
#思路：做一个嵌套，然后前后对比，如果[j]大于（小于）[i],那么就在g（l）数列的i
#位置记录一次，表明他大于（或者小于）过之前的数字一次。而当之前再有发生大于（小于）
#的时候，如果在该位置上有记录，那说明之前已经有过一次大于（小于），所以再发生一次
#那么刚好就是3次，然后把j位置的大于（小于）发生次数加到答案上就可以了。