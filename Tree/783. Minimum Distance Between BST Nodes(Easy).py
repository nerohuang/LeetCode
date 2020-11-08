# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.store = []
        self.ans = float('inf');
        
        def dfs(node):
            self.store.append(node.val);
            if node.left:
                dfs(node.left);
            
            if node.right:
                dfs(node.right);
                
        dfs(root)
        
        self.store.sort();
        
        for i in range(1, len(self.store)):
            self.ans = min(self.ans, self.store[i] - self.store[i - 1])
        
        return self.ans;