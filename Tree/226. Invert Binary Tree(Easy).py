# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left);
            return root;

#思路依旧是用递归往最深处找，然后找到尽头便可以直接交换
#其他语言要新建一个TreeNode的class的变量来储存，要不然直接调换会失去原先左边的分支
#example：
#public class Solution {
#    public TreeNode invertTree(TreeNode root) {
#        if(root == null) return null;
#        TreeNode tmp = root.left;
#        root.left = invertTree(root.right);
#        root.right = invertTree(tmp);
#        return root;
#    }
#}

#其他方法
## BFS 广度优先搜索
#def invertTree2(self, root):
#    queue = collections.deque([(root)])
#    while queue:
#        node = queue.popleft()
#        if node:
#            node.left, node.right = node.right, node.left
#            queue.append(node.left)
#            queue.append(node.right)
#    return root
#    
## DFS 深度搜索优先
#def invertTree(self, root):
#    stack = [root]
#    while stack:
#        node = stack.pop()
#        if node:
#            node.left, node.right = node.right, node.left
#            stack.extend([node.right, node.left])
#    return root