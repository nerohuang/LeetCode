# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def countDepth(root):
            if not root:
                return 0
            left = countDepth(root.left);
            right = countDepth(root.right);
            return 1 + max(left, right)
        return countDepth(root);

#一左一右往深处找，没有就返回0
#递归，每一层加1，返回结果