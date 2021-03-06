class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0, 1];
        while len(ans) <= num:
            ans += [x + 1 for x in ans];
        return ans[:num + 1]

#这道题的思路前提是要找到规律：
#十进制：           0 1
#二进制有几个1：     0 1
# 0 | 1 | 2 3 | 4 5 6 7 | 8 9 10 11 12 13 14 15
# 0 | 1 | 2 3 | 1 2 2 3 | 1 2 2 3   2  3  3  4
#我们可以看到，这种分组的情况下，第i组里面的数的二进制
#含1的个数是i-1组的个数 + i-1组的个数+1.
#| 4 5 6  7 
#| 1 2 2  3  
# ------------------------
#| 8 9 10 11 12 13 14 15
#| 1 2 2  3   2  3  3  4
#这样看就会明显一点
#同时我们可以继续简化成 i 组的就是之前所有数字的二进制
#含1的个数+1
# 0 | 1 | 2 3 | 4  5  6  7
# 0 | 1 | 2 3 | 1  2  2  3
#-------------------------------
# 8  9   10 11 12 13 14 15
# 1  2   2  3  2  3  3  4
#这样就清楚了。
#然后只要ans这个数组的长度小于输入的数字
#那么不管他直接进行扩展，然后直接输出到ans[num + 1]
#就可以了，因为要包含0