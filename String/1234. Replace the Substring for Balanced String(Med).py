from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        need = Counter(s) - Counter({a: len(s)//4 for a in 'QWER'});
        n = len(s);
        if need == Counter():
            return 0;
        
        left, right = 0, 0;
        needLen = len(need);
        vaild = 0;
        ans = n;
        window = {"Q":0, "W":0, "E":0, "R":0};
        
        def compare(window, remain):
            for c in remain:
                if window[c] < remain[c]:
                    return False;
            return True;
        
        while right < n:
            window[s[right]] += 1;
            right += 1;
            
            while compare(window, need):
                ans = min(ans, right - left)
                window[s[left]] -= 1;
                left += 1;
            
        return(ans)

#思路：
#统计出来然后找到比平均数高的组，然后用slide window
#关于slide window的思路：
#每一个right pointer经过的字母都计算一次。
#然后检查当前window里面的字母的出现次数是不是都大于了
#需要改变的次数（就是大于该字母出现总数减去平均数）。
#如果都大于了，那么先求出当前window的长度
#然后left pointer的字母减少1，并将left pointer向右
#移动一位。