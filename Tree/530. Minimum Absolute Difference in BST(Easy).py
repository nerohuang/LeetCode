# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        store = [];
        if not root:
            return 0;
        
        def findPath(root, store):
            store.append(root.val);
            
            if root.left:
                findPath(root.left, store);
            
            if root.right:
                findPath(root.right, store);
                
        
        findPath(root, store);
        
        store.sort()
        
        print(store)
        
        ans = float("inf");
        
        for i in range(1, len(store)):
            if abs(store[i] - store[i - 1]) <= ans:
                ans = abs(store[i] - store[i - 1])
                
        return ans;

#思路：找任意node之间的绝对值最小差

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#class Solution:
#    def getMinimumDifference(self, root: TreeNode) -> int:
#        def inorder(node):
#            nonlocal min_diff, prev
#            if not node:
#                return False
#            # inorder : left -> root -> right
#            inorder(node.left)
#            if prev != None:
#                min_diff = min(min_diff, node.val - prev)
#            prev = node.val
#            inorder(node.right)
#            
#        min_diff = float('inf')
#        prev = None
#        inorder(root)
#        return min_diff