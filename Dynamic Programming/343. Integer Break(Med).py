class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)];
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]));
        return dp[n]

#思路：
#典型的DP问题
#建立一个DP数组表示dp[i]为在数字i的时候能得到
#的最大乘积。
#然后以i为index从3开始遍历，因为1和2答案都是1
#不用管，然后遍历的同时还要用以j为index遍历一
#遍从1到i，并进行判断：
#max(j * (i - j), j * dp[i - j])
#首先计算拆分为两个数字的乘积，
#即j乘以 i-j，然后是拆分为多个数字的情况，
#这里就要用到 dp[i-j] 了，这个值表示数字 i-j 
#任意拆分可得到的最大乘积，再乘以j就是数字i
#可拆分得到的乘积，取二者的较大值来更新 dp[i]，
#最后返回 dp[n] 即可


#数学解法：
#题目提示中让用 O(n) 的时间复杂度来解题，而且告诉我们找7到 10 之间的规律，
# 么我们一点一点的来分析：
#正整数从1开始，但是1不能拆分成两个正整数之和，所以不能当输入。
#那么2只能拆成 1+1，所以乘积也为1。
#数字3可以拆分成 2+1 或 1+1+1，显然第一种拆分方法乘积大为2。
#数字4拆成 2+2，乘积最大，为4。
#数字5拆成 3+2，乘积最大，为6。
#数字6拆成 3+3，乘积最大，为9。
#数字7拆为 3+4，乘积最大，为 12。
#数字8拆为 3+3+2，乘积最大，为 18。
#数字9拆为 3+3+3，乘积最大，为 27。
#数字10拆为 3+3+4，乘积最大，为 36。
#....
#那么通过观察上面的规律，我们可以看出从5开始，数字都需要先拆出所有的3，
# 一直拆到剩下一个数为2或者4，因为剩4就不用再拆了，拆成两个2和不拆没
# 有意义，而且4不能拆出一个3剩一个1，这样会比拆成 2+2 的乘积小。
# 这样我们就可以写代码了，先预处理n为2和3的情况，然后先将结果 res 
# 初始化为1，然后当n大于4开始循环，结果 res 自乘3，n自减3，根据之前
# 的分析，当跳出循环时，n只能是2或者4，再乘以 res 返回即可：
