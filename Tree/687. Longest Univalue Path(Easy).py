# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int: 
        
        self.longest = 0
        
        def uniValuePathToRoot(root): 
            if not root: 
                return 0 

            if not root.left and not root.right: 
                return 0 
            
            left = uniValuePathToRoot(root.left)
            right = uniValuePathToRoot(root.right)
            
            #如果左边是空或者和根不相等但右边和根相等的话那么就对比看看是不是比当前答案大，然后因为相等所以返回右子叶的统计+1；
            if not root.left or root.val != root.left.val: 
                if root.right and root.val == root.right.val: 
                    self.longest = max(self.longest, right+1)
                    return right+1
                else: 
                    return 0 
            
            #如果右边是空或者和根不相等但左边和根相等的话那么就对比看看是不是比当前答案大，然后因为相等所以返回左子叶的统计+1；
            if not root.right or root.val != root.right.val: 
                if root.left and root.val == root.left.val: 
                    self.longest = max(self.longest, left+1)
                    return left+1
                else: 
                    return 0 
                
            #如果左右子叶和根相等，那么最长就是左右+2，因为有两个相等的，然后和答案比较，但只返回左右中最大的+1，因为是寻找最大的答案。
            if root.left.val == root.right.val: 
                if root.val == root.left.val: 
                    self.longest = max(self.longest, left+right+2)
                    return max(left, right)+1
                else: 
                    return 0 
            
        uniValuePathToRoot(root)
        
        return self.longest