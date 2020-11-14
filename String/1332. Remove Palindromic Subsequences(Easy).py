class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0;
        elif s == s[::-1]:
            return 1;
        else:
            return 2;
        
#思路:
#脑筋急转弯，因为只有两个字母，所以如果本身是回文就1
#不是那么最多就是2，因为只要第一次把a删掉，第二次再把b删掉就可以了。