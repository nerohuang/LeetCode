# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def preorder(node):
            if node.left:
                node.left.par = node;
                preorder(node.left);
            if node.right:
                node.right.par = node;
                preorder(node.right);
        preorder(root);
        
        root.par = None  # 补充根节点的父节点为空
        nodes = [target]  # 每一层的节点列表，初始化为距离=0层，即target节点本身
        seen = {target}  # 已发行节点列表
        for _ in range(K):
            temp = []
            for node in nodes:  # 处理当前层每个节点，找寻其下一层且未发现的节点
                for n in (node.left, node.right, node.par):
                    if n and n not in seen:
                        seen.add(n)
                        temp.append(n)
            nodes = temp
        return [n.val for n in nodes]

# BFS
# 不过需要加上一个新的pra属性代表这个node的parent是啥
# 然后其他用bfs的思路遍历就可以了。
# 遍历距离为k，然后把k的val输出就行了。