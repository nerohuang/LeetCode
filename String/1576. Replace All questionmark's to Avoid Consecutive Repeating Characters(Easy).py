class Solution:
    def modifyString(self, s: str) -> str:
        ans = list(s);
        
        alphabet = "abcdefghijklmnopqrstuvwxyz";
        
        if len(s) == 1 and s =="?":
            return "a";
        
        for i in range(len(s)):
            if s[i] == "?":
                if i == 0:
                    for c in alphabet:
                        if c != ans[i + 1]:
                            ans[i] = c;
                            break;
                elif i > 0 and i < len(s) - 1:
                    for c in alphabet:
                        if c != ans[i + 1] and c !=ans[i - 1]:
                            ans[i] = c;
                            break;
                elif i == len(s) - 1:
                    for c in alphabet:
                        if c != ans[i - 1]:
                            ans[i] = c;
                            break;
                            
        return "".join(ans);