class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        strings = [str(num) for num in A];
        stringA = "".join(strings);
        intA = int(stringA);
        ans = intA + K;
        stringAns =str(ans);
        return [char for char in stringAns]

##class Solution:
##    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
##        
##        
##        
##        # my solution ... 
##        #  time: O(n)
##        # space: O(1)
##        
##        carry, j = 0, len(A)-1
##        while j >= 0 and K > 0:
##            d = K % 10
##            K //= 10
##            dnew = A[j] + d + carry
##            carry, A[j] = dnew // 10, dnew % 10
##            j -= 1
##        if j == -1:
##            left = []
##            while K > 0:
##                d = K % 10
##                K //= 10
##                dnew = d + carry
##                carry, dnew = dnew // 10, dnew % 10
##                left.append(dnew)
##            if carry:
##                left.append(carry)
##            return left[::-1] + A
##        if carry:
##            while carry and j >= 0:
##                dnew = A[j] + carry
##                carry, A[j] = dnew // 10, dnew % 10
##                j -= 1
##            if carry:
##                A = [carry] + A
##        return A