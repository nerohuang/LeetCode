# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        store = [];
        def inorder(node):
            if not node:
                return
            
            store.append(str(node.val));
            if node.left:
                inorder(node.left);
            if node.right:
                inorder(node.right);
        
        inorder(root);
        
        print(store)
            
        return '-'.join(store); 

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        
        def insert(root, node):
            if not root:
                return TreeNode(node);
            
            if node <= root.val:
                root.left = insert(root.left, node);
            else:
                root.right = insert(root.right, node);
            
            return root;
        
        root = None;
        if data:
        
            nodeList = data.split('-');
            root = TreeNode(int(nodeList[0]));
            nodeList.pop(0);
            for node in nodeList:
                root = insert(root, int(node));
        
        return root


#其实是没什么难度的一题
#第一部就是考察preorder，如何遍历一个BST，然后生成一个文件
#第二部就是将第一步生成的文件还原回树。