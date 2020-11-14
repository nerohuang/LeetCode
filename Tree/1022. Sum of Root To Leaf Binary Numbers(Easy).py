# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        store = [];
        
        def build(node, binary):
            if node.right != None:
                build(node.right, binary + str(node.val));
            if node.left:
                build(node.left, binary + str(node.val));
            if not node.right and not node.left:
                print(binary + str(node.val))
                store.append(binary + str(node.val));
        
        
        build(root, "")
        ans = 0;
        for binary in store:
            ans += int(binary, 2);
        
        return ans