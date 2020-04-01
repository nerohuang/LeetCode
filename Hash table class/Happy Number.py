class Solution:
    def isHappy(self, n: int) -> bool:
        a = []
        sumn = 0
        while n not in a:
            a.append(n)
            for x in str(n):
                sumn = sumn + (int(x)**2)
            n = sumn
            sumn = 0
        if n==1:
            return True
        else:
            return False