# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = [];
        store = [];
        store.append(root);
        storeVal = [];
        while store:
            for node in store:
                if node:
                    storeVal.append(node.val);
            ans.append(max(storeVal));
            storeVal = [];
            
            curLen = len(store);
            for i in range(curLen):
                node = store.pop(0);
                if node.left:
                    store.append(node.left);
                if node.right:
                    store.append(node.right);
        return ans

#BFS