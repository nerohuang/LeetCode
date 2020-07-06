mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]];
k = 3;


#class Solution:
#    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#        return sorted(range(len(mat)), key = lambda x : sum(mat[x]))[:k];

import heapq

#class Solution:
#	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
res, q = [], []
for i in range(len(mat)):
	heapq.heappush(q,(mat[i].count(1),i))
for i in range(k):
	res.append(heapq.heappop(q)[1])
print(res)

#heapq --- 堆队列算法
#这个模块提供了堆队列算法的实现，也称为优先队列算法。

#堆是一个二叉树，它的每个父节点的值都只会小于或大于所有孩子节点（的值）。它使用了数组来实现：
# 从零开始计数，对于所有的 k ，都有 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]。 
# 为了便于比较，不存在的元素被认为是无限大。 堆最有趣的特性在于最小的元素总是在根结点：heap[0]。

#heapq.heappush(heap, item)
#将 item 的值加入 heap 中，保持堆的不变性。
#
#heapq.heappop(heap)
#弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。