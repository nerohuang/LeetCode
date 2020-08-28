# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def preorder(root):
            if not root:
                return "";
            if not root.left and not root.right:
                return str(root.val);
            if not root.right:
                return str(root.val) + "(" + preorder(root.left) + ")";
            return str(root.val) + "(" + preorder(root.left) + ")" + "(" + preorder(root.right) + ")";
        
        return preorder(t);

#思路其实就是前序遍历，然后分各种情况来确定括号位置