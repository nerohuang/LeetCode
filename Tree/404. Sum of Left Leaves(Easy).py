# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        
        leftNode = []
        left = False;
        def findLeaf(root, leftNode, left):
            
            
            if root.left:
                left = True
                findLeaf(root.left, leftNode, left);
                
            if root.right:
                left = False
                findLeaf(root.right, leftNode, left);
            
            if not root.left and not root.right and left:
                leftNode.append(root.val);
        
        findLeaf(root, leftNode, left)
        
        return sum(leftNode)

#思路：标记一下当前的点是不是在左边，如果是而且没有子叶就记录