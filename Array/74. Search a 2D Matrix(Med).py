class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True;
        return False;

#class Solution:
#    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#        k=-1
#        
#        # if matrix is empty or if matrix is not the input
#        if not matrix:
#            return False
#        row,col=len(matrix),len(matrix[0])
#        if row*col==0:
#            return False
#        
#        # if target is not in searching range
#        if matrix[0][0]>target or target > matrix[row-1][col-1]:
#            return False
#
#        # identifying the row in which target is needed to be searched 
#        for i in range(row):
#            if matrix[i][0]<= target and matrix[i][col-1]>=target:
#                k=i
#        
#        if k==-1:
#            return False
#
#
#        # number is searched in the corresponding row using binary search
#        l,h=0,col-1
#        while l<=h:
#            mid= l + (h-l)//2
#            if matrix[k][mid]==target:
#                return True
#            elif matrix[k][mid]<target:
#                l=mid+1
#            else:
#                h=mid-1
#        return False