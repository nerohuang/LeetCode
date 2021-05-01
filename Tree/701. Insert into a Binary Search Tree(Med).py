# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val, None, None)
        def insert(node, val):
            if node.val < val:
                if node.right:
                    insert(node.right, val);
                else:
                    node.right = TreeNode(val, None, None);
            elif node.val > val:
                if node.left:
                    insert(node.left, val);
                else:
                    node.left = TreeNode(val, None, None);
        
        insert(root, val);
        return root
# BST