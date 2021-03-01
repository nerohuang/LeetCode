# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections;

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        store = collections.defaultdict(int);
        
        def dfs(node):
            if not node:
                return 0;
            
            left = dfs(node.left);
            right = dfs(node.right);
            
            store[node.val + right + left] += 1;
            
            return node.val + right + left;
        
        dfs(root);
        if not store:
            return [];
        
        maxFreq = max(store.values());
        ans = [];
        for key, value in store.items():
            if value == maxFreq:
                ans.append(key);
        
        return ans;

#卧槽defaultdict！卧槽DFS！
#用defaultdict先建立一个dict,然后用dfs遍历!
#就是：
#1.获得左子树的sum
#2.获得右子树的sum
#3.获得当前node的值！
#所以当前node的total sum就是：
#leftSUM + rightSUM + node.val！
#如果node不存在，返回0就可以了!