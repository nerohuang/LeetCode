# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def order(node):
            if not node:
                return None;
            
            node.left = order(node.left);
            node.right = order(node.right);
            
            if not node.val and not node.left and not node.right:
                node = None;
            
            return node;
        
        return order(root)

# 思路
# 递归（Recursion）
# 因为他是要求我们去除所有的子节点只有0或者空的节点
# 那么很简单就用递归
# 如果节点本身为空就返回空，判断完之后进入一左一右。
# 因为要重新塑造树，所以我们要把左右子节点都重新赋
# 予下一次递归返回的新值。
# 在完成递归之后，我们再判断当前的node是否有子节点
# 和他的值是否为0，如果是，那么当前node就变成空并
# 返回，如果不是，那么返回原样。