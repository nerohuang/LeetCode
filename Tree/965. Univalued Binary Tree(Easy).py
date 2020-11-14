# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        num = root.val;
        self.univalued = True;
        
        def dfs(node):
            if node:
                if node.val != num:
                    self.univalued = False;
                if node.left:
                    dfs(node.left);
                if node.right:
                    dfs(node.right);
        
        dfs(root);
        return self.univalued