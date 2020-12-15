# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = [];
        
        def postOrder(node):
            if not node:
                return;
            if node.left:
                postOrder(node.left);
            if node.right:
                postOrder(node.right);
            ans.append(node.val);
        
        postOrder(root);
        
        return ans;