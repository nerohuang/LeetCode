# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(remainIn):
            if remainIn != []:
                newNode = TreeNode();
                newNode.val = postorder[0];
        
                indexIn = remainIn.index(postorder[0]);
        
                leftIn = remainIn[:indexIn];
                rightIn = remainIn[indexIn + 1:];
        
                postorder.pop(0);
                
                
                newNode.right = build(rightIn);
                newNode.left = build(leftIn);
        
                return newNode;
        
        postorder = postorder[::-1];
        return build(inorder);