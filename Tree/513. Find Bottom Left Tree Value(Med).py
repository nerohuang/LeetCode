# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        store = [];
        store.append(root);
        mostLeft = -1;
        while store:
            curLen = len(store);
            for i in range(curLen):
                node = store.pop(0);
                    mostLeft = node.val;
                if node.left:
                    store.append(node.left);
                if node.right:
                    store.append(node.right);
        return mostLeft

#用BFS做
#注意的是他要最左边的
#所以按照BFS的思路，每一次开始循环的第一个就是该深度的
#第一个。所以记录下来就可以。