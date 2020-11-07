# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def pre_order(root, tree):
            if root:
                tree.append("," + str(root.val));
                pre_order(root.left, tree);
                pre_order(root.right, tree);
            else:
                tree.append("null")
            return tree;
        
        sTree = "".join(pre_order(s, []));
        tTree = "".join(pre_order(t, []));
        if (sTree.find(tTree) != -1):
            return True;
        else:
            return False;
            