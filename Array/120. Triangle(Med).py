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
# For the kth level:
# minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i]; 
# 然后最后得出的第一位就是答案
# 其实就是反推，从下往上，然后找到每一层的最小数字存储就行了。
# 比如我们从【4 1 8 3】开始，然后回到上一层【6 5 7】
# 那么从[6 5 7]的角度看，要找到下一步的最少就是
# min(ans[i], ans[i + 1]) + triangle[layer][i];
# 然后取代原来的ans
# 比如【6 5 7】下一步最少的就是【7 6 10 3】
# 那个3就不用管了，所以每往前回溯一层就能抛去掉一个数字
# 所以最后返回第一位也就是回溯到第一层唯一留存的有效数字
# 就可以了
