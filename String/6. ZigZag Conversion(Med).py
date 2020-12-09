class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        store = [["" for _ in range(len(s))]for _ in range(numRows)];
        i = 0;
        m, n = -1, 1;
        while i < len(s):
            if m == -1:
                m += 1;
                n -= 1;
                while m < numRows:
                    if i < len(s) and store[m][n] == "":
                        store[m][n] = s[i];
                        i += 1;
                    m += 1;
            if m == numRows:
                m -= 2;
                n += 1;
                while m >= 0:
                    if i < len(s):
                        store[m][n] = s[i];
                        m -= 1;
                        n += 1;
                        i += 1;
                    else:
                        break;
         
        ans = ""
        for i in range(len(store)):
            for c in store[i]:
                if store[i] != "":
                    ans += c
            
        return(ans)


#class Solution:
#    def convert(self, s: str, numRows: int) -> str:
#        if numRows == 1:
#            return s
#        
#        lines = [''] * numRows
#        line_count = 0
#        adder = 1
#        for c in s:
#            lines[line_count] = lines[line_count] + c
#            
#            if line_count + adder > numRows-1:
#                adder = -1
#            elif line_count + adder < 0:
#                adder = 1
#            
#            line_count = line_count + adder
#        return ''.join(lines)