mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 4;


m = len(mat);
n = len(mat[0]);
lessSide = min(m, n);
ans = 0;

for i in range(lessSide, 0, -1):
    for y in range(0, n - i + 1):
        for x in range(0, m - i + 1):
            matrixSum = 0;
            for j in range(i):
                matrixSum += sum(mat[x + j][y:y + i]);
            if matrixSum <= threshold:
                print(i);
                break;

if ans == 0:
    print(0);



## GET DIMENSIONS
#nrows, ncols = len(mat), len(mat[0])
## SETUP THE PREFIX SUM MATRIX
#prefix = [[0 for _ in range(ncols + 1)] for _ in range(nrows + 1)]
#
## FILL THE CELLS - TOP RECT + LEFT RECT - TOP LEFT DOUBLE-COUNTED RECT
#for i in range(nrows):
#    for j in range(ncols):
#        prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + mat[i][j]
#
## for row in prefix:
##     print(row)
#    
#'''
#1. INITIALIZE MAX_SIDE = 0
#2. AT EACH CELL, WE'LL CHECK IF RECTANGLE (OR SQUARE) FROM [I - MAX, J - MAX] TO [I, J], BOTH INCLUSIVE, IS <= THRESHOLD
#'''
#
## INITIALIZE MAX SIDE
#max_side = 0
#
## CHECK IF RECTANGLE (OR SQUARE) FROM [I - MAX, J - MAX] TO [I, J] <= THRESHOLD
#for i in range(nrows):
#    for j in range(ncols): 
#        
#        # CHECK IF WE CAN SUBTRACT MAX_SIDE
#        if min(i, j) >= max_side:
#            curr = prefix[i + 1][j + 1]
#            top = prefix[i - max_side][j + 1]
#            left = prefix[i + 1][j - max_side]
#            topLeft = prefix[i - max_side][j - max_side]
#            total = curr - top - left + topLeft
#            
#            # print(f"CURR : {curr} | TOP : {top} | LEFT : {left} | TOP_LEFT : {topLeft}")
#            # print(f"TOTAL : {total}\n")
#            
#            # UPDATE MAX_SIDE IFF TOTAL <= THRESHOLD
#            if total <= threshold:
#                max_side += 1
#        
## RETURN MAX SIDE
#print(max_side)

#思路是prefix sum, 还是比较巧妙，怎么想到这个累加关系以及位置关系比较重要。。。
#思路看
#https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/discuss/698422/Python-Prefix-Sum-(Explanation-with-Diagram)
#还有
#https://www.cnblogs.com/seyjs/p/12082483.html