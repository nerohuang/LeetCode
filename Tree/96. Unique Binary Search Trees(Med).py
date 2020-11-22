class Solution:
    def numTrees(self, n: int) -> int:
        # numTree[4] = numTree[0] * numTree[3] +
        #              numTree[1] * numTree[2] +
        #              numTree[2] * numTree[1] +
        #              numTree[3] * numTree[0]
        numTree = [1] * (n + 1)
        
        # 0 nodes = 1 tree
        # 1 nodes = 1 tree
        #因为0和1个node只有一种可能，所以不用计算，所以从2到n+1（因为要计算到
        #第n个）
        for nodes in range(2, n + 1):
            total = 0
            #因为所有的node都会做一次root，所以遍历他们，从1个node开始到node。
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
            
        return numTree[n]
