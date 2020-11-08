# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        self.ans = TreeNode();
        self.null = True;
        
        def find(node, val):
            if not node:
                return
            if node.val == val:
                self.ans = node;
                self.null = False
            if node.left:
                find(node.left, val);
            if node.right:
                find(node.right, val);
        
        find(root, val);
        
        if self.null:
            return (None);
        else:
            return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#class Solution:
#    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#        l = root
#        while l:
#            if l.val == val:
#                return l
#            elif l.val > val:
#                l = l.left
#            else:
#                l = l.right
#        return None
#这种做法的思路就是因为是BST所以左<中<右