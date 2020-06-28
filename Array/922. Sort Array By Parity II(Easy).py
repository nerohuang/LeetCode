class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = [0 for i in range(len(A))];
        eveni = 0;
        oddi = 1;
        for num in A:
            if num % 2 ==0:
                result[eveni] = num;
                eveni += 2;
            else:
                result[oddi] = num;
                oddi += 2;
        return result;

##class Solution:
##    def sortArrayByParityII(self, A: List[int]) -> List[int]:
##        j = 1
##        for i in range(0, len(A), 2):
##            if A[i] % 2:
##                while A[j] %2:
##                    j += 2
##                A[i], A[j] = A[j], A[i]
##        return A