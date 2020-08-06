# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True;
        if not q or not p:
            return False;
        if p.val != q.val:
            return False;
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#The simplest strategy here is to use recursion. Check if p and q nodes are not None, 
#and their values are equal. If all checks are OK, do the same for the child nodes 
#recursively.