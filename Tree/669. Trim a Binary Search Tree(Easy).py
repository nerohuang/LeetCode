# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return None;
            elif node.val > high:
                return trim(node.left);
            elif node.val < low:
                return trim(node.right);
            else:
                node.left = trim(node.left);
                node.right = trim(node.right);
                return node
        
        
        return trim(root);
            
#重点是记住BST，左子叶 < 根 < 右子叶 就很好理解了。
#如果当前 根 大于high，那么就把他的左子叶接上去，反之亦然。