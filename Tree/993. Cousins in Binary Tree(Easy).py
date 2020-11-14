# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        find = [];
        def findNode(node, depth, num):
                    
            if node.right and node.right.val == num:
                find.append([node.val, depth + 1])
            elif node.left and node.left.val == num:
                find.append([node.val, depth + 1])
                    
            if node.left: findNode(node.left, depth + 1, num);
            if node.right: findNode(node.right, depth + 1, num);
            
            
        findNode(root, 0, x);
        findNode(root, 0, y);
        if len(find) == 1:
            return False;
        if find[0][0] != find[1][0] and find[1][1] == find[0][1]:
            return True
        else:
            return False
    

#class Solution:
#    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
#        
#        queue = deque()
#        queue.append((root, None, 0))
#        x_depth, x_parent = 0, None 
#        y_depth, y_parent = 0, None 
#        
#        while queue:
#            node, parent, depth = queue.popleft()
#            
#            if node.val == x:
#                x_depth = depth 
#                x_parent = parent
#            elif node.val == y:
#                y_depth = depth 
#                y_parent = parent
#        
#            if x_depth > 0 and y_depth > 0:
#                if x_depth == y_depth:
#                    if x_parent == y_parent: return False
#                    else: return True
#                else:
#                    return False
#            
#            if node.left: queue.append((node.left, node, depth+1))
#            if node.right: queue.append((node.right, node, depth+1))
#            
#        return False
#更快的思路：用DFS