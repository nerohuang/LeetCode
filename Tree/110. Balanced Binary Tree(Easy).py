# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def countDepth(root):
            if not root:
                return 0;
            
            left = countDepth(root.left);
            right = countDepth(root.right);
            if left == -1 or right ==  -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right);
        
        return True if countDepth(root) != -1 else False;

#104变体，找出左右树深度是否不超过1；依旧是先找深度，然后对比left和right，只要左右深度超过1，
#就返回-1。最终结果查看深度返回值是-1还是非-1，如果是-1说明深度差别已经超过1，false；