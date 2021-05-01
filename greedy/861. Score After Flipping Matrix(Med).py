class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)): #setting the first element  to 1 in each row will always result in a larger summation
            if A[i][0] == 0:
                for j in range(len(A[i])):
                    A[i][j] = 1 if A[i][j] == 0 else 0
        n = 0
        for j in range(len(A[0])): #for each column, if the number of 0 is larger than the number of one, then do the toggling process
            # 计算每一列有多少个1
            count = sum([A[i][j] for i in range(len(A))])
            # max(count,len(A)-count)就是找到1多还是0多，然后取
            # 更多的，因为谁更多变换成1之后就是1最多
            # 然后后面*2**(len(A[0])-j-1)就算计算该为从
            # 二进制变为十进制的数字，因为二进制的计算关系
            # 只要计算某一位然后加起来就完事了。
            n+= max(count,len(A)-count)*2**(len(A[0])-j-1)
    
        return n

# 一个很巧妙的greedy的题目
# 一开始可能觉得很复杂，不过要想想怎么取得二进制最大值就很好理解
# 因为二进制要最大，首先保证首位为1，因为只要第一位是1那么之后就算是0
# 都比第一位是0后面全是1大。
# 然后变换第一位，如果第一是1就不用翻转，如果不是就反转
# 这样就可以初步保证最大的，然后我们要尽可能取大，那么只能在后面的
# 数位做文章。因为我们可以反转列，那么我们从第二列开始：
# 如果那一列的1的个数比0的个数多，那么就不用反转，反之，翻转
# 这样就能得到每列更多的1，最后变成这个矩阵里面每行有更多的1
# 也就得到更大的和。