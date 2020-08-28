# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0;
        def findDepth(root):
            if root:
                L = findDepth(root.left);
                R = findDepth(root.right);
                self.ans = max(self.ans, L + R);
                return max(L, R) + 1
            else:
                return 0;
            
        findDepth(root);
        return self.ans

#思路：其实就是找出根节点左右子叶的最大深度相加就可以了。