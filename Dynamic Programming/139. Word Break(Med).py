class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)];
        dp[0] = True;
        
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True;
                    break;
        
        return dp[-1]

#思路：
#新建一个DP数组，长度为len(s)-1，除了第一个全部为False;
#遍历整个s所有可能的substirng
#右指针为i，左指针为j
#如果dp[j]为True，s[j:i]在wordDict里面，那么dp[i]就改为True：
#dp[j]为True才能继续是为了保证在j位之前的substring都或多或少可以被break
#并存在与wordDict里面。
#意思是从第j到i位之间的substring在wordDict里面，然后break，不用再寻找；
#i往前一位然后j重新遍历。
#最后如果输出dp[-1]，如果全部可break，那么那时候dp[-1]应该是True
#要不然就是False
