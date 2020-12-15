# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.store = [];
        self.i = 0;
        
        def inorder(node):
            if not node:
                return;
            if node.left:
                inorder(node.left);
            self.store.append(node.val);
            if node.right:
                inorder(node.right);
            
        inorder(root);
        
        self.count = len(self.store);

    def next(self) -> int:
        self.i += 1;
        return self.store[self.i - 1];
        

    def hasNext(self) -> bool:
        if self.i < self.count:
            return True;
        else:
            return False;
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()