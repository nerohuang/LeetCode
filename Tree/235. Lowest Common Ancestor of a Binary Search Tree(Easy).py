# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findNode(root, p, q):
            if not root:
                return None;
            
            if root.val > p.val and root.val > q.val:
                return findNode(root.left, p, q);
            
            if root.val < q.val and root.val < p.val:
                return findNode(root.right, p, q);
            
            return root;
        
        return findNode(root, p, q);

#思路： 由于是BST，所以左小于中，中小于右，可以利用这一点，如果p和q都是小中的话，那么意思
#是那个结点在左边，反之在右边，而如果夹在p和q中间的话，那么当前节点就是答案。