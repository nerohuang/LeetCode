# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        store = [];
        def findPath(node, count, path):
            if node:
                if count - node.val == 0 and not node.left and not node.right:
                    path += str(node.val)
                    store.append(path);
                else:
                    path += str(node.val) + " "
                    if node.left:
                        findPath(node.left, count - node.val, path);
                    if node.right:
                        findPath(node.right, count - node.val, path);
        
        
        findPath(root, sum, "")
        ans = [];
        for path in store:
            ans.append(path.split(" "))
        return ans;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#class Solution:
#    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#        store = [];
#        def findPath(node, count, path):
#            if node:
#                if count - node.val == 0 and not node.left and not node.right:
#                    path.append(node.val)
#                    store.append(path.copy());
#                    path.pop()
#                    return 
#                else:
#                    
#                    if node.left:
#                        path.append(node.val)
#                        findPath(node.left, count - node.val, path);
#                        path.pop()
#                    if node.right:
#                        path.append(node.val)
#                        findPath(node.right, count - node.val, path);
#                        path.pop()
#        
#        
#        findPath(root, sum, [])
#        return store;
##用数组的记录方法
#数组要用copy来重开一个