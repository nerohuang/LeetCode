class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0;
        preI = 0;
        for j in range(1, len(A)):
            ans = max(A[j] - j + A[preI] + preI, ans);
            if A[j] + j > A[preI] + preI:
                preI = j;
        return ans

#一般暴力解法是两重循环，即先找到一个位置 i 之后，从其后位置 j 继续循环遍历，这样的复杂度是
#O(N ^ 2) 的。看到题目给出的数据范围，数组的长度是 50000， 对于这个题O(N ^ 2) 的时间复杂度
#肯定不可取。
#
#对于这个题，我们知道肯定只能用 O(N) 的解法，把公式稍加变化成(A[i] + i) + (A[j] - j)，我们
#可以看出要找出这两部分和的最大值。
#
#具体方法是保存每个位置 j ，时刻维护其前面的A[i] + i的最大值出现的位置 pre_i。最后结果就是对
#于每个位置j对应的A[i] + A[j] + i - j最大值。