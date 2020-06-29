class Solution:
    def fib(self, N: int) -> int:
        FibSeq = [0 , 1];
        if N >= 2:
            for i in range(1, N):
                FibSeq.append(FibSeq[i - 1] + FibSeq[i]);
        return FibSeq[N];


##class Solution:
##    def fib(self, N: int) -> int:
##        if N > 1:
##            memo = [-1]*(N+1)
##            return self.fib_helper(N, memo)
##        return N
##    
##    def fib_helper(self, N, memo):
##        if N == 0 or N == 1:
##            return N
##        if memo[N] == -1:
##            memo[N] = self.fib_helper(N-1, memo) + self.fib_helper(N-2, memo)
##        return memo[N]