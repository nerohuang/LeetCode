class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        ALen = len(A);
        minright = [A[-1]] * ALen;
        for i in range(ALen - 2, -1, -1):
            minright[i] = min(minright[i + 1], A[i]);
        
        maxLeft = -float('inf');
        for i in range(ALen - 1):
            maxLeft = max(maxLeft, A[i]);
            if maxLeft <= minright[i + 1]:
                return i + 1

#Let's try to find max(left) for subarrays left = A[:1], left = A[:2], left = A[:3], 
#... etc. Specifically, maxleft[i] will be the maximum of subarray A[:i]. They are 
#related to each other: max(A[:4]) = max(max(A[:3]), A[3]), 
#so maxleft[4] = max(maxleft[3], A[3]).
#
#Similarly, min(right) for every possible right can be found in linear time.
#
#After we have a way to query max(left) and min(right) quickly, the solution is 
#straightforward.
#
#3 passes solution:
#first pass: use an array to keep the maximun of all left element,
#second pass: use an array to keep the minimun of all right element,
#third pass: find where the maxleft <= minright:
#
#    def partitionDisjoint(self, A):
#       maxleft = [A[0]]*len(A)
#       for i in range(1,len(A)):
#           maxleft[i] = max(maxleft[i-1], A[i])
#           
#       minright = [A[-1]]*len(A)
#       for i in range(len(A)-2,-1,-1):
#           minright[i] = min(minright[i+1], A[i]) 
#       
#       for i in range(len(A)-1):
#           if maxleft[i] <= minright[i+1]:
#               return i+1
#2 passes solution:
#skip the first maxleft pass, keep only the minright array, and use maxleft as a variable:
#
#    def partitionDisjoint(self, A):
#       minright = [A[-1]]*len(A)
#       for i in range(len(A)-2,-1,-1):
#           minright[i] = min(minright[i+1], A[i]) 
#
#       maxleft = -float('inf')
#       for i in range(len(A)-1):
#           maxleft = max(maxleft, A[i])  
#           if maxleft <= minright[i+1]:
#               return i+1
#1 pass solution:
#use one more variable leftmax to moniter:
#
#    def partitionDisjoint(self, A):
#       disjoint = 0
#       curmax = leftmax = A[0]
#       for i,num in enumerate(A):
#           curmax = max(curmax, num)
#           if num < leftmax:
#               leftmax = curmax
#               disjoint = i
#       return disjoint + 1 