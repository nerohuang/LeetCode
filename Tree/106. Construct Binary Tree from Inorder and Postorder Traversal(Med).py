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

# 思路和105是一样的
# 不过要先把postorder顺序换一下，因为
# postorder 顺序是 lll rrrr m
# 所以以postorder顺序调一下就是
# m rrrr lll
# 这样m就变回第一个了，不过同样的左右树也要换一下
# 先后，因为左右树在上面那个调换的同时也一起调转了