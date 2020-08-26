# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
            
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return [];
        ans = [];
            
        def findPath(root, ans, curAns):
            curAns += str(root.val);
            
            if root.left:
                findPath(root.left, ans, curAns + "->");
                
            if root.right:
                findPath(root.right, ans, curAns + "->");
        
            if not root.left and not root.right:
                ans.append(curAns); 
                
        
        findPath(root,ans, "");
        
        return ans

#思路其实和前面是一样的，找到尽头而已。。。。
#太久没做了傻了