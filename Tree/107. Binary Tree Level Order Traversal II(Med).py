# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return [];
        
        ans = [];
        queue = [root]
        
        while len(queue) != 0:
            layer = [];
            for i in range(len(queue)):
                curVal = queue.pop(0);
                layer.append(curVal.val);
                if curVal.left != None:
                    queue.append(curVal.left);
                if curVal.right != None:
                    queue.append(curVal.right);
            ans.insert(0, layer);
        
        return ans;

#由于题目遍历顺序是前序，所以按照中左右顺序遍历
#所以先把第一个（root）放入一个储存队列queue，然后弹出queue第一个值并插入该深度的队列layer，
# 然后判断该node有没有左子叶和右子叶。有的话插入储存序列queue，然后循环到queue完全清空为止。