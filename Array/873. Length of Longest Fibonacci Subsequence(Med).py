#class Solution:
#    def lenLongestFibSubseq(self, A: List[int]) -> int:
#        s = set(A)
#        ans = 0;
#        for i in range(len(A) - 1):
#            for j in range(i + 1, len(A)):
#                num1 = A[i];
#                num2 = A[j];
#                count = 2;
#                while (num1 + num2 in s):
#                    num1, num2 = num2, num1 + num2;
#                    count += 1;
#                ans = max(ans, count);
#        return ans if ans >=3 else 0;
#
#def lenLongestFibSubseq(self, A):

import collections

A = [1,2,3,4,5,6,7,8]

dp = collections.defaultdict(int)
s = set(A)
for j in range(len(A)):
    for i in range(j):
        if A[j] - A[i] < A[i] and A[j] - A[i] in s:
            dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
print(max(dp.values() or [0]));

#Another solution is kind of dp.
#dp[a, b] represents the length of fibo sequence ends up with (a, b)
#Then we have dp[a, b] = (dp[b - a, a] + 1 ) or 2
#The complexity reduce to O(N^2).
#In C++/Java, I use 2D dp and index as key.
#In Python, I use value as key.