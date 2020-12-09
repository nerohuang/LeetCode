# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        store = [];
        
        def preorder(node, num):
            if node:
                num = num * 10 + node.val;
                if not node.left and not node.right:
                    store.append(num);
                if node.left:
                    preorder(node.left, num);
                if node.right:
                    preorder(node.right, num);
            
        preorder(root, 0);
        return (sum(store))