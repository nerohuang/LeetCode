class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) < len(str2):
            str1, str2 = str2, str1;
        
        x = str2;
        for i in range(len(str2)):
            if str2.replace(x,"") == "" and str1.replace(x, "") == "":
                return x;
            x = x[:-1]
        
        return x;


#
#class Solution:
#    def gcdOfStrings(self, str1: str, str2: str) -> str:
#        import math
#        
#        x = str1
#        m = len(str1)
#        n = len(str2)
#               
#        
#        def divides(x, k):
#            # if  m % k != 0 or n % k != 0:
#            #     return False
#            # # print(x * (m // k), x * (n // k))
#            if str1 == x * (m // k) and str2 == x * (n // k):
#                return True
#            return False
#        
#        if len(str1) > len(str2):
#            x = str2
#        
#        k = math.gcd(m,n)
#        if k >= 1:
#            x = str1[:k]
#            if divides(x, k):
#                return x
#            
#        
#        return ""
#思路：先求出最大公约数，然后再裁剪就可以了。