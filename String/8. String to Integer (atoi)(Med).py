class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0;
        
        s = s.strip();
        
        pos = True;
        
        if s and s[0] == "+":
            s = s[1:];
        elif s and s[0] == "-":
            s = s[1:];
            pos = False;
        
        num = 0;
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c);
            else:
                break;
        
        if pos:
            if num >= (2**31):
                return (2**31)-1
            else:
                return num
        elif not pos:
            if -num < -(2**31):
                return -(2**31)
            else:
                return -num