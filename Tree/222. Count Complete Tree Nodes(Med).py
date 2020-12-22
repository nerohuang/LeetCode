# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.ans = 0;
        
        def preorder(node):
            if node:
                self.ans += 1;
                
                if node.left:
                    preorder(node.left);
                if node.right:
                    preorder(node.right);
        
        
        preorder(root)
        return self.ans

#更快的思路：
#因为是完美二叉树，所以先找到最深处最左边的节点还有最右边节点的深度
#如果两边深度一样，那么总节点数就是 2^h - 1
#如果不一样，那么就用递归累加。
#class Solution:
#    def countNodes(self, root: TreeNode) -> int:
#        
#        def recursion(root):
#            def ldepth(root):
#                ans = 0
#                while root:
#                    ans+=1
#                    root=root.left
#                return ans
#            def rdepth(root):
#                ans = 0
#                while root:
#                    ans+=1
#                    root=root.right
#                return ans
#            if not root:
#                return 0
#            l = ldepth(root.left)
#            r = rdepth(root.right)
#            if l==r:
#                return pow(2,l+1)-1
#            right = recursion(root.right)
#            left = recursion(root.left)
#            return left+right+1
#        return recursion(root)