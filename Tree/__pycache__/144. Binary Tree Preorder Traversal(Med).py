# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return [];
        
        ans = [];
        
        def pre(node):
            if node:
                ans.append(node.val);
                if node.left:
                    pre(node.left);
                if node.right:
                    pre(node.right);
        
        pre(root);
        return ans