# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0;
    
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right);
            self.total += root.val;
            root.val = self.total;
            self.convertBST(root.left);
        
        return root





#思路：后序遍历，因为右子叶一直大于左子叶和根，然后从最右子叶开始一直sum，然后替代当前node
#即可。


#function引入的两种全局变量的用法

#class Solution:
#    
#    def convertBST(self, root: TreeNode) -> TreeNode:
#        self.total = 0;
#        def sumNode(root):
#            if root:
#                sumNode(root.right);
#                self.total += root.val;
#                root.val = self.total;
#                sumNode(root.left);
#                
#        sumNode(root)
#        
#        return root


#class Solution:
#    
#    
#    def convertBST(self, root: TreeNode) -> TreeNode:
#        total = [0];
#        def sumNode(root, total):
#            if root:
#                sumNode(root.right,total);
#                total[0] += root.val;
#                root.val = total[0];
#                sumNode(root.left, total);
#        
#        sumNode(root, total)
#        
#        return root