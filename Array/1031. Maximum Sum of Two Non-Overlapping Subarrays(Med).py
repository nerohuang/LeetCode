class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i - 1];
        
        res = A[L + M - 1];
        Lmax = A[L - 1];
        Mmax = A[M - 1];
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - M - L]);
            Mmax = max(Mmax, A[i - L] - A[i - M - L]);
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L]);
        return res

#动态规划
#凡是要求数组某一段的和，要想到用pre_sum，pre_sum[i]表示指数i之前左右数的和。
#这样我们要求A[i]到A[j]之间所有数的和，就可以用pre_sum[j] - pre_sum[i - 1]
#回到这道题，我们第一遍遍历数组A求pre_sum。
#
#第二遍遍历，指数为i，用max_L记录指数i - M之前的最大连续L个数之和，
#每次更新max_L为max(max_L, pre_sum[i - M] - pre_sum[i - L - M])
#max_L + pre_sum[i] - pre_sum[i - M]表示以i结尾最后连续M个数，与之前最大的连续L个数的和。
#因为 M 数组也可以在 L 前面，所以还要调转判断一次
#同理max_M + pre_sum[i] - pre_sum[i - L]就表示以i结尾最后连续L个数，与之前最大的连续M个数
#的和。
#取其中较大的与最终要返回的值res比较，并更新即可。

#两种情况：
#
#       找到max_L      长度M的区间   
#|_____________________|______|_________________|
#                             i
#
#       找到max_M      长度L的区间   
#|_____________________|______|_________________|
#                             i
#