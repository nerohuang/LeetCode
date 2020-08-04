class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        def cmp(a, b):
            if a > b:
                return -1;
            if a == b:
                return 0;
            if a < b:
                return 1;
            
            
        ans = 1;
        record = 0;
        compare = -2;
        for i in range(1, len(A)):
            compare = cmp(A[i - 1], A[i]);
            if compare == 0:
                record = i;
            elif (i == len(A) - 1) or (cmp(A[i], A[i + 1]) != -compare):
                ans = max(ans, i - record + 1);
                record = i;
        return ans;

#Evidently, we only care about the comparisons between adjacent elements. 
#If the comparisons are represented by -1, 0, 1 (for <, =, >), then we want 
#the longest sequence of alternating 1, -1, 1, -1, ... (starting with either 1 or -1).
#
#These alternating comparisons form contiguous blocks. We know when the next 
#block ends: when it is the last two elements being compared, or when the 
#sequence isn't alternating.
#
#For example, take an array like A = [9,4,2,10,7,8,8,1,9]. The comparisons are 
#[1,1,-1,1,-1,0,-1,1]. The blocks are [1], [1,-1,1,-1], [0], [-1,1].
#
#其实就是对比，A[i]和A[i - 1]对比，如果A[i - 1] > A[i]记录为-1， A[i- 1] < A[i]记录为1，
#A[i - 1] = A[i]记录为0，最长距离就是保持记录为[1，-1，1，-1....]或者[-1，1，-1，1....]；
#当是0或者有相同趋势的时候重新记录。