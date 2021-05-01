# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def build(remainIn):
            if remainIn != []:
                newNode = TreeNode();
                newNode.val = preorder[0];
        
                indexIn = remainIn.index(preorder[0]);
        
                leftIn = remainIn[:indexIn];
                rightIn = remainIn[indexIn + 1:];
        
                preorder.pop(0);
        
                newNode.left = build(leftIn);
                newNode.right = build(rightIn);
        
                return newNode;
        
        return build(inorder);

# 思路：
# 其实看preorder和inorder的排序然后按照遍历顺序分开就行了：
# preorder : m lllll rrrrrr
# inorder: lllll m rrrrr
# 所以我们每pop出一个preorder 的第一个数字，就能以他为中心
# 在inorder处切割一左一右分别进去m node的左子树和右子树
# 然后一直递归到空就可以了。