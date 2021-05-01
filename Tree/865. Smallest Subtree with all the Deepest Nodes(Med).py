# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (None, 0);
            l = dfs(node.left);
            r = dfs(node.right);
            #计算深度
            depth = max(l[1], r[1]) + 1;
            #比较深度，返回比较深得
            if l[1] > r[1]:
                return (l[0], depth);
            elif l[1] < r[1]:
                return (r[0], depth);
            #深度一样返回根节点
            return (node, depth)
        
        return dfs(root)[0]

# 思路
# dfs
# 因为要找到最深的node，所以用dfs
# 然后记录每一个node的深度，只保留最深的就可以了
# 如果深度一样，那么就返回他的根节点。