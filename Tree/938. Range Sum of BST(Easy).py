# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0;
        
        def dfs(node):
            if node and node.val >= low and node.val <= high:
                self.ans += node.val;
            if node.left:
                dfs(node.left);
            if node.right:
                dfs(node.right);
        
        dfs(root);
        
        return self.ans;




#class Solution:
#    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
#        
#        def dfs(node):
#            if node: 
#                if low <= node.val <= high: 
#                    self.ans += node.val
#                if low < node.val: 
#                    dfs(node.left)
#                if node.val < high: 
#                    dfs(node.right)
#        self.ans = 0
#        dfs(root)
#            
#        return self.ans
#更快得思路，还是BST得特性：左《中《右