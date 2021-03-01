class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = triangle[-1];
        for layer in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[layer])):
                ans[i] = min(ans[i], ans[i + 1]) + triangle[layer][i];
        return ans[0]


# 一个从后往前想会更容易地DP
#其实已经想出来了
#比如例子  [[2],[3,4],[6,5,7],[4,1,8,3]]
#可以看成
#       3
#     7 8
#   4 5 1
# 2 3 6 4
# 所以先把【4 1 8 3】最为最底层然后往前推，公式是下面
#For the kth level:
#minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i]; 
#然后最后得出的第一位就是答案
