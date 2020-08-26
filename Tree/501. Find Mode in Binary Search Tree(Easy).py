# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            
    def findMode(self, root: TreeNode) -> List[int]:
        store = {};
        res = []
        
        if not root:
            return []
        
        def findEle(root, store):
            if root.val not in store:
                store[root.val] = 1;
            else:
                store[root.val] += 1;
                
            if root.left:
                findEle(root.left, store);
            if root.right:
                findEle(root.right, store);
        
        findEle(root, store);
        maxNode = max(store, key = store.get)
        
        
        for node in store:
            if store[node] == store[maxNode]:
                res.append(node);
        
        return res

#找出现过最多次的node
