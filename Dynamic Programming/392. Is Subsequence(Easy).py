class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sI = 0;
        tI = 0;
        tLen = len(t);
        while sI < len(s):
            if t[tI:tLen].find(s[sI]) != -1:
                tI += t[tI:tLen].find(s[sI]) + 1;
                sI += 1
            else:
                return False
        if sI == len(s):
            return True
        else:
            return False

#class Solution:
#    def isSubsequence(self, s: str, t: str) -> bool:
#        m, n = len(s), len(t)
#        
#        if m > n: return False
#        if m == n: return s == t
#        
#        i = j = 0
#        while i < m and j < n:
#            if s[i] == t[j]:
#                i += 1
#                j += 1
#            else:
#                j += 1
#                
#        return i == m