class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sumA = sum(A);
        if sumA % 3 != 0:
            return False;
        else:
            count = 0;
            partSum = 0;
            for num in A:
                partSum += num;
                if partSum == sumA / 3:
                    count += 1;
                    partSum = 0;
        return True if count >= 3 else False;

##class Solution:
##    def canThreePartsEqualSum(self, A: List[int]) -> bool:
##        total = sum(A)
##        if total % 3 != 0:
##            return False
##        target = total // 3
##        count = 0
##        accu = 0
##        for i in range(len(A)):
##            accu += A[i]
##            if accu == target:
##                count += 1
##                accu = 0
##            if count == 2:
##                break
##        
##        return count == 2 and i <len(A) - 1