# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0;
        def count(root):
            if root:
                L = count(root.left);
                R = count(root.right);
                self.ans += abs(L - R)
                return (root.val + L + R);
            else:
                return 0
            
        count(root);
        return self.ans

#思路：草，题目意思我都不知道怎么表达
#这道题让我们求二叉树的坡度，某个结点的坡度的定义为该结点的左子树之和与右子树之和的差的绝对值，
#这道题让我们求所有结点的坡度之和。
#所以依旧递归找答案就可以了