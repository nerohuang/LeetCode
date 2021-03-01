class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, root, None)
        store = [root];
        level = 1;
        while level < d - 1:
            storeLen = len(store);
            for i in range(storeLen):
                node = store.pop(0);
                if node.left:
                    store.append(node.left);
                if node.right:
                    store.append(node.right);
            level += 1
            
        for node in store:
            node.left = TreeNode(v, node.left, None);
            node.right = TreeNode(v, None, node.right);
        return root
    
# BFS,DFS都行
# 想法是对的，实现很差
# 其实就是首先遍历到深度d的上一个深度d-1
# 并记录下那个深度的node
# 然后遍历所有记录的node，并给所有node新建一个
# sub node
# 左边就是 TreeNode(v, node.left, None)
# 右边就是 TreeNode(v, None, node.right)
# 因为加了那一层v之后，原来左右两边的subnode会
# 继承在之前加的subnode（也就是d）的同一方向。
# 就是：
#          4                  4
#        /  \               /   \
#       2    6    ->       2     6
#      / \    \           / \    / \ 
#     3   5   7          1   1  1   1
#     v = 1 d = 3       /     \      \
#                      3       5      7