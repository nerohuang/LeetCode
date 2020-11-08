897. Increasing Order Search Tree# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        store = [];
        
        def inorder(node):
            if node.left:
                inorder(node.left);
            if node:
                store.append(node.val);
            if node.right:
                inorder(node.right);
        
        
        inorder(root);
        
        store.sort();
        

        #==================以下是重点====================
        ans = cur = TreeNode();
        ans.val = store[0];
        print(ans)
        
        
        for i in range(1, len(store)):
            cur.right = TreeNode(val = store[i]);
            cur = cur.right
            
        return ans;
            
#重点是构建新的树，要用一个sentinel去暂存并推进树的层数但又不丢失位置。