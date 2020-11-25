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