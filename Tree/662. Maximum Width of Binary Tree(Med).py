# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0;
        
        queue = [(root, 0)];
        maxWidth = 1;
        
        while queue:
            print(queue)
            maxWidth = max(maxWidth, queue[-1][1] - queue[0][1] + 1);
            
            tempQueue = [];
            while queue:
                node, width = queue.pop(0);
                if node.left:
                    tempQueue.append((node.left, 2*width));
                if node.right:
                    tempQueue.append((node.right, 2*width + 1));
        
            queue = tempQueue;
        
        return maxWidth

# 思路：BFS
# 可以先画出一个完整的BST，然后看看规律
# 比如每行第一个node是0，第二个是1，第三个是2
# 可以得到
#           0
#        /    \
#       0      1
#      /\    /  \
#     0  1   2   3
#    /\  /\  /\  /\
#   0  1 2 3 4 5 6 7 
# 可以看到 left subtree 的位置是父节点乘以 2
# right subtree 是父节点乘以 2 然后 + 1
# 所以就算有空缺的，只要一前一后剪掉就能得到总长度。
# 然后就用bfs做就可以了。