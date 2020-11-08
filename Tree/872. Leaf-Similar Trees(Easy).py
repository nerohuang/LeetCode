# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        root1Store = [];
        root2Store = [];
        
        def findLeaf(node, store):
            if not node:
                return
            if node.left:
                findLeaf(node.left, store);
            if node.right:
                findLeaf(node.right,store);
            if not node.left and not node.right:
                store.append(node.val);
            
            return store;
        
        root1Store = findLeaf(root1, []);
        root2Store = findLeaf(root2, []);
        
        return root1Store == root2Store;

#思路：后序遍历如果没有子叶的节点就加上