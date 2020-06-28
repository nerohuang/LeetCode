class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        eleStore = {};
        for num in deck:
            if num not in eleStore.keys():
                eleStore[num] = 1;
            else:
                eleStore[num] += 1;
        minCount = min(eleStore.values());
        for i in reversed(range(1,minCount+1)):
            if list(filter(lambda j: j%i!=0,eleStore.values())) == []:
                hcf = i;
                break;
        if hcf > 1:
            return True;
        else:
            return False;

##from collections import Counter
##from functools import reduce
##
##class Solution:
##    def hasGroupsSizeX(self, deck: List[int]) -> bool:
##        v = list(Counter(deck).values())
##        
##        def gcd(a, b):
##            while b:
##                a, b = b, a%b
##            return a
##        
##        return reduce(gcd, v) > 1