# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        def Build(arr):
            if arr:
                maxIndex = arr.index(max(arr));
                node = TreeNode(arr[maxIndex], None, None);
                left = arr[:maxIndex];
                right = arr[maxIndex + 1:];
            
                node.left = Build(left);
                node.right = Build(right);
            
                return node;
            else:
                return None
        
        return Build(nums);

# 递归
# 没什么好说的。。。