# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0;
        
        def findSum(node, path):
            if not node:
                return 0;
            
            path.append(node.val);
            print(path)
            curSum = 0;
            count = 0;
            for i in range(len(path) - 1, -1, -1):
                curSum += path[i];
                if curSum == sum:
                    count += 1;
            print(count)
            
            count += findSum(node.left, path);
            count += findSum(node.right, path);
            
            path.pop();
            
            return count;
        
        return findSum(root, []);


#思路：
#DFS，然后中间插入的是从后往前的累加
#为什么是从后往前是因为这次寻找sum并不是一定要从顶点开始
#所以从后往前遍历才行。
#然后每次返回当前路径能有多少和sum一样的。