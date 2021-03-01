class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pstore = [];
        qstore = [];
        
        
        def ppath(root, node):
            if not root:
                return False;
            pstore.append(root);
            if root == node:
                return True;
            TF = False;
            if root.left:
                TF = ppath(root.left, node);
            if not TF and root.right:
                TF = ppath(root.right, node);
            if not TF:
                pstore.pop();
            return TF;
        
        def qpath(root, node):
            if not root:
                return False;
            qstore.append(root);
            if root == node:
                return True;
            TF = False;
            if root.left:
                TF = qpath(root.left, node);
            if not TF and root.right:
                TF = qpath(root.right, node);
            if not TF:
                qstore.pop();
            return TF;
            
            
        
        ppath(root, p);
        qpath(root, q);
        
        for i in range(min(len(pstore), len(qstore))):
            if pstore[i] == qstore[i]:
                ans = pstore[i];
                
        return ans

#这里是要记住怎么寻找根节点倒给定节点的路径。
#思路是用一个数组记录，然后先找左边，如果找到就返回true
#如果左边找不到，而且右边不为空就找右边，如果找不到，就返回false
#并弹出最后一个放入stack的node

#class Solution:
#    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#        
#        # found p and q?
#        if not root or root == p or root == q:
#            return root
#        
#        
#        left = self.lowestCommonAncestor(root.left, p, q)
#        right = self.lowestCommonAncestor(root.right, p, q)
#        
#        # p and q appears in left and right respectively, then their ancestor is root
#        if left is not None and right is not None:
#            return root
#        
#        # p and q not in left, then it must be in right, otherwise left
#        if left is None:
#            return right
#        
#        if right is None:
#            return left
#
#更快的做法：
#因为是寻找最小共同父节点，所以要知道有三种可能：
#1. p和q分别位于左右子树中，那么对左右子节点分别递归，就会找到p和q的位置
#而当前节点就正好是p和q的最小共同父节点。
#2. 当p和q都在左子树的时候，那么会返回p和q比较高的那个到left，然后right
#为空。这时候left就是答案。
#3. 反过来当p和q都在右子树，那么会返回p和q比较高的那个到right，然后left
#为空，这时候right就是答案。
