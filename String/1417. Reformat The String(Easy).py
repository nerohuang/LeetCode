class Solution:
    def reformat(self, s: str) -> str:
        alphabet = [];
        number = [];
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                alphabet.append(c);
            else:
                number.append(c);
        ans = ""
        aCount = 0;
        nCount = 0;
        if abs(len(alphabet) - len(number)) <= 1:
            while len(ans) != len(s):
                if len(alphabet) >= len(number):
                    if aCount < len(alphabet):
                        ans += alphabet[aCount];
                    if nCount < len(number):
                        ans += number[nCount];
                    aCount += 1;
                    nCount += 1;
                else:
                    if nCount < len(number):
                        ans += number[nCount];
                    if aCount < len(alphabet):
                        ans += alphabet[aCount];
                    aCount += 1;
                    nCount += 1;
        
        return ans

#class Solution:
#    def reformat(self, s: str) -> str:
#        a1 = list(filter(str.isalpha, s))
#        a2 = list(filter(str.isdigit, s))
#
#        if abs(len(a1) - len(a2)) > 1:
#            return ""
#        
#        if len(a1) < len(a2):  # ensure len(a1) >= len(a2)
#            a1, a2 = a2, a1
#        
#        result = [c for t in zip(a1, a2) for c in t] + a1[len(a2):]
#        
#        return "".join(result)

#zip和filter的用法