class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def buildIP(cur, remain, long):
            
            if long == 4:
                if len(cur) == len(s) + 3:
                    ans.append(cur[:]);
                return;
            
            for i in range(1, min(len(remain) + 1, 4)):
                new = remain[:i];
                if 0 <= int(new) < 256 and not(new[0] == "0" and len(new) > 1):
                    if not cur:
                        buildIP(new, remain[i:], long + 1);
                    else:
                        buildIP(cur + "." + new, remain[i:], long + 1);
        
        ans = [];
        buildIP("", s, 0);
        
        return ans

#思路：
#用DFS做：
#因为IP每一段是1到4位，所以就遍历
#从1位到s剩余的最多的位
#然后因为是数字，所以开头不能是0.
#当找完4个之后，如果还有剩余，那么就不能加进答案
#因为要刚好。
