import math;

n = 13
A = [float("inf") for _ in range(n + 1)]
A[0] = 0
for j in range(1, n + 1):
	for i in range(1, int(math.floor(math.sqrt(j))) + 1):
		A[j] = min(A[j], 1 + A[j - i**2])
return A[-1];

#一个DP思路:
#先创建n+1长度的数组，除了第一位为0，其他都是无限大。
#然后从1遍历到n+1为j，然后嵌套，从1遍历到sqrt(j)
#然后A[j]表示j最少可以用多少个平方数相加
#A[J -I**2] + 1意思是在j减去可能的平方数得出的差
#所需的平方数目+1.
#最后返回最后一个就是结果。
#dp[5] = min{
#dp[5 – 2 * 2] + 1 = dp[1] + 1 = (dp[1 – 1 * 1] + 1) + 1 = dp[0] + 1 + 1 = 2,
#dp[5 – 1 * 1] + 1 = dp[3] + 1 = (dp[3 – 1 * 1] + 1) + 1 = dp[1] + 2 = dp[1 – 1*1] + 1 + 2 = dp[0] + 3 = 3
#};