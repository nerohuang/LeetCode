# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        store = set();
        def travel(node):
            store.add(node.val);
            if node.left:
                travel(node.left);
            if node.right:
                travel(node.right);
                
        travel(root)
        allVal = list(store);
        allVal.sort();
        if len(allVal) >= 2:
            return allVal[1];
        else:
            return -1

    