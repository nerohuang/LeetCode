# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        store = {};
        count = {};
        depth = 0;
        res = [];
        def sumLevel(root, depth):
            if root:
                if depth not in store:
                    store[depth] = root.val;
                    count[depth] = 1;
                else:
                    store[depth] += root.val;
                    count[depth] += 1;
            if root.left:
                sumLevel(root.left, depth + 1);
            if root.right:
                sumLevel(root.right, depth + 1);
            
        sumLevel(root, depth)    
        
        print(store)
        
        for i in sorted(store):
            res.append(store[i]/count[i])
            
        return res;

#思路：累计同一深度的node的总和并计算有多少个node，然后输出