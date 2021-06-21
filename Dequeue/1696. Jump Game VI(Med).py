class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        decQueue = [ (nums[0], 0) ]     #单调递减队列
        res = nums[0]
        for i in range(1, n):
            while decQueue and i - decQueue[0][1] > k:  #扔掉左侧已经index超出范围的
                decQueue.pop(0)
            res = decQueue[0][0] + nums[i]              #贪心，计算当前的最大结果
            while decQueue and decQueue[-1][0] <= res:  #维持单调递减的性质(容易错！！！一开始写成nums[i]了)
                decQueue.pop(-1)
            decQueue.append( (res, i) ) 
        
        return res

# 思路：
# dp + heap建立维持一个单调递减的数列
# 思路是以nums[i] + decQueue里面的第一位，因为
# decqueue是个单调递减，所以第一位肯定是最大的
# 第一个while是抛出值直到在范围k为止
# 然后用当前数字Nums[i] + decqueue里面的最大值decQueue[0][0]
# 得出res
# 接着第二个while就是维持一个单调递减的queue
# 所以从后往前， 如果decQueue[-1][0] <= res
# 那么就抛出
# 最后把新的res加入