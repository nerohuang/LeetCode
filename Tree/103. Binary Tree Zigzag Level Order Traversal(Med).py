# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [];
        def store(node, depth):
            if node:
                if len(ans) <= depth:
                    ans.append([node.val]);
                else:
                    ans[depth].append(node.val)
                if node.left:
                    store(node.left, depth + 1);
                if node.right:
                    store(node.right, depth + 1);
        
        store(root, 0);
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i] = ans[i][::-1]
        return ans;