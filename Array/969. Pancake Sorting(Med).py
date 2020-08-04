class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = [];
        for i in range(len(A), 1, -1):
            idx = A.index(i);
            ans.extend([idx + 1, i]);
            A = A[:idx + 1][::-1] + A[idx + 1:];
            A = A[:i][::-1];
        return ans;

#Find max
#swap max to top
#swap max to bottom
#reduce size
#repeat
#
#[3,2,4,1]
#[4,2,3,1]
#[1,3,2,4]
#[3,1,2,4]
#[2,1,3,4]
#[1,2,3,4]
#
#Explanation
#Find the index i of the next maximum number x.
#Reverse i + 1 numbers, so that the x will be at A[0]
#Reverse x numbers, so that x will be at A[x - 1].
#Repeat this process N times.