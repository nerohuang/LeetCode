#class Solution:
#    def largestOverlap(self, A, B):
#        """
#        :type A: List[List[int]]
#        :type B: List[List[int]]
#        :rtype: int
#        """
#        d = collections.defaultdict(int)
#        a = []
#        b = []
#        for i in range(len(A)):
#            for j in range(len(A[0])):
#                if(A[i][j] == 1):
#                    a.append((i,j))
#                if(B[i][j] == 1):
#                    b.append((i,j))
#        ans = 0
#        for t1 in a:
#            for t2 in b:
#                t3 = (t2[0]-t1[0],t2[1]-t1[1])
#                d[t3] += 1
#                ans = max(ans, d[t3])
#        return ans
#
#1. For each pair of 1's you can make from all the 1's in A and B
#2. Record the vector/translation/tuple that points from pointA to 
#pointB (e.g. take component-wise difference, this represents the 
#translation to get pointA and pointB to align)
#3. Keep track of how many points in A and B correspond to the different 
#translations (e.g. 2 points have translation (0, 1), 3 points have 
#translation (-1, 4), .... etc.)
#4. Choose the translation that has the most points that get aligned 
#(e.g. the most frequent translation/vector you see when taking differences)