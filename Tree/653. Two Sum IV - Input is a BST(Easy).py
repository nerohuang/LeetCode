# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        store = [];
        def travel(node):
            store.append(node.val);
            if node.left:
                travel(node.left);
            if node.right:
                travel(node.right);
        
        travel(root);
        
        for i in range(len(store) - 1):
            for j in range(i + 1, len(store)):
                if store[i] + store[j] == k:
                    return True;
        
        return False


#class Solution:
#    def findTarget(self, root: TreeNode, k: int) -> bool:
#        st = set()
#        
#        q = collections.deque()
#        
#        q.append(root)
#        
#        while q:
#            cur = q.popleft()
#            if cur.val in st:
#                return True
#            st.add(k-cur.val)
#            if cur.left: q.append(cur.left)
#            if cur.right: q.append(cur.right)
#            
#        return False