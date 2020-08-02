A = [3,2,1,2,1,7]

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        ans = 0;
        numCount = {};
        for i in range(len(A)):
            while A[i] in numCount:
                A[i] += 1;
                ans += 1;
            numCount[A[i]] = 1;
        return ans;


#res = need = 0
#A.sort();
#for i in A:
#    res += max(need - i, 0)
#    need = max(need + 1, i + 1)
#
#Sort the input array.
#Compared with previous number,
#the current number need to be at least prev + 1.