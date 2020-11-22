# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.TF = True;
        def vaild(node, lower = float("-inf"), upper = float("inf")):
            if node.val <= lower or node.val >= upper:
                self.TF = False;
            if node.left:
                if node.left.val < node.val:
                    vaild(node.left, lower, node.val);
                else:
                    self.TF = False;
            if node.right:
                if node.right.val > node.val:
                    vaild(node.right, node.val, upper);
                else:
                    self.TF = False;
        
        vaild(root)
        return self.TF;


#思路：直接对比，但要有两个变量分边记录某一边的BST的最大值和最小值。
#如果左边大于那个最大值或者左边小于那个最小值也不行。
#那个最大/最小值其实就是那一节的root，而相对于左边而言root是最大值
#相对于右边而言root是最小值。

#https://leetcode.com/problems/validate-binary-search-tree/solution/