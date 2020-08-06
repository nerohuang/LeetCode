# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None;
        
        mid = len(nums) // 2;
        
        root = TreeNode(nums[mid]);
        root.left = self.sortedArrayToBST(nums[:mid]);
        root.right = self.sortedArrayToBST(nums[mid + 1:]);
        
        return root;

#思路：
#先寻找每一个根，因为题目要求是高度平衡，所以就是当前数组找出中位，然后一左一右循环做。