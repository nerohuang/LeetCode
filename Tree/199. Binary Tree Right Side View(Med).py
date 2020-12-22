# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return ""
        store = [];
        
        store.append(root);
        ans = [];
        
        while store:
            ans.append(store[-1].val);
            nextLevel = [];
            for node in store:
                if node.left:
                    nextLevel.append(node.left);
                if node.right:
                    nextLevel.append(node.right);
            store = nextLevel;
        
        return ans

#BFS