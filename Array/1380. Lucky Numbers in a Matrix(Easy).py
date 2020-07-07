##class Solution:
##    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
##        result = [];
##        import numpy as np;
##        matrixNp = np.array(matrix);
##        for row in matrix:
##            index = row.index(min(row));
##            if max(matrixNp[:, index]) == row[index]:
##                result.append(row[index]);
##        return result;

#class Solution:
#    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
#        return list(set([min(row) for row in matrix]).intersection(set([max(row) for row in zip(*matrix)])))