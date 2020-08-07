# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def countSum(root, totalSum, result):
            if not root:
                result.append(totalSum);
                return
            
            totalSum += root.val;
            if None in [root.left, root.right]:
                if root.left == None and root.right != None:
                    right = countSum(root.right, totalSum, result);
                    return
                elif root.right == None and root.left != None:
                    left = countSum(root.left, totalSum, result);
                    return
            left = countSum(root.left, totalSum, result);
            right = countSum(root.right, totalSum, result);
        
        result = [];
        countSum(root, 0, result);
        print(result)
        return True if sum in result else False

#思路是综合104找depth还有Array里面40求Sum而来，先把所有sum找到，然后对比看看给出的有没有。
#而且和111一样要对末端进行判断，以免出错算多了。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#class Solution:
#    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#        if not root:
#            return False
#        stack = [root]
#        while stack:
#            current = stack.pop()
#            if current.val == sum and not current.left and not current.right:
#                return True
#            
#            if current.left:
#                current.left.val += current.val
#                stack.append(current.left)
#                
#            if current.right:
#                current.right.val += current.val
#                stack.append(current.right)
#                
#        return False