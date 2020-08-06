# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1: TreeNode, t2: TreeNode):
            if not t1 and not t2:
                return True;
            if not t1 or not t2:
                return False;
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left);
        
        return isMirror(root, root);


#A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
#
#Push an element in stack
#
#Therefore, the question is: when are two trees a mirror reflection of each other?
#
#Two trees are a mirror reflection of each other if:
#
#Their two roots have the same value.
#The right subtree of each tree is a mirror reflection of the left subtree of the other 
#tree.
#Push an element in stack
#
#This is like a person looking at a mirror. The reflection in the mirror has the same 
#head, but the reflection's right arm corresponds to the actual person's left arm, and 
#vice versa.
#
#The explanation above translates naturally to a recursive function as follows.