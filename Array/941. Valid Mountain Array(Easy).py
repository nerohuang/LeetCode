class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        top = 0;
        for i in range(len(A) - 1):
            if A[i] == A[i + 1]:
                return False;
            elif A[i] > A[i + 1]:
                top = i;
                break;
        if top == 0:
            return False;
        else:
            for i in range(top, len(A) - 1):
                if A[i] <= A[i + 1]:
                    return False;
        return True;

##class Solution:
##    def validMountainArray(self, A: List[int]) -> bool:
##        if A == [] or len(A) == 1 or len(A) == 2:
##            return False
##        peak = -inf
##        for i, num in enumerate(A):
##            if num > peak:
##                peak = num
##            else:
##                break
##        if peak == A[0] or peak == A[-1]:
##            return False
##  
##        for j in range(i, len(A)):
##            if A[j] >= peak:
##                return False
##            else:
##                peak = A[j]
##        return True