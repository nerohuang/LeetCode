class Solution:
    def numDecodings(self, s: str) -> int:
        
        ans = [1] + [int(s[0]) != 0] + [0] * (len(s) - 1);
        
        for i in range(1, len(s)):
            if int(s[i]):
                ans[i + 1] = ans[i];
            if 9 < int(s[i - 1: i + 1]) < 27:
                ans[i + 1] += ans[i - 1];
        
        return int(ans[-1])

#思路，建立一个以[1]为开始的dp
#然后开始判断：如果第一位不是0的话，那么往dp里面append一个[1]：
#[1, 1]
#然后开始遍历：
#先判定s[i]是不是0，如果不是，dp[i] = dp[i + 1]，因为这个题目是
#寻找有多少种解密方式，所以各位数的话那么只有一种，延续dp[i-1]的种类
#然后判断s[i - 1:i + 1]是不是在10和26之间：
#如果是，那么代表出现了两位数的decode，此时的种类就会比单纯的个位数多
#一种，所以是要往前一位的种类数+1，dp[i - 1] + 1 = dp[i + 1] 
#维护的dp数组长度始终比s多1.