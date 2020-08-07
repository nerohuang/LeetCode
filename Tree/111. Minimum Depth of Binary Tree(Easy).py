# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def countDepth(root):
            if not root:
                return 0;
            
            left = countDepth(root.left);
            right = countDepth(root.right);
            
            if None in [root.left, root.right]:
                return 1 + max(left, right);
            else:
                return 1 + min(left, right);
        
        return countDepth(root);

#依旧是104的思路，重点是当发现某个根的子叶不存在的时候，就要换成max，要不然的话会判断出
#错，比如
#   1
#  / 
# 2
#不改判断的话会因为右子叶为null而判断最大深度为1，其实应该是2.