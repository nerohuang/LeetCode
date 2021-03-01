# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMin(self, root):
        current = root;
        while current.left:
            current = current.left;
        return current
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root;
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key);
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key);
            
        else:
            if not root.left and not root.right:
                root = None;
            
            elif not root.left:
                root = root.right;
            
            elif not root.right:
                root = root.left;
            
            else:
                temp = self.findMin(root.right);
                root.val = temp.val;
                root.right = self.deleteNode(root.right, temp.val);
        
        return root
                

#思路就是分三种：
#因为是BST，所以 左 < 中 < 右
#所以当前node比key大，那么往左找，反之往右找。
#当找到这个node的时候，也有三种可能:
#1. 没有左右sub node的时候，直接删掉
#2. 如果只有左边或者右边，往上接上去就行了
#3. 但如果两边都有，那么我们只需要找右子树里面最小的然后把最小的代替
#要去掉的，或者反过来找左子树的最大值代替
#因为BST里面右边总比左边大。
#当代替完之后，把要寻找的那个数换成已经代替掉的，并继续遍历下去。