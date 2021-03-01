# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        path = collections.defaultdict(int);
        ans = [];
        
        def dfs(node):
            if node:
                uid = str(node.val) + dfs(node.left) + dfs(node.right);
                if path[uid] == 1:
                    print(ans)
                    ans.append(node);
                path[uid] += 1;
            else:
                uid = "*";
            return uid
        
        dfs(root);
        return ans

#只能说collection里面的defauldict是个神器。。
#思路其实就是dfs然后找出那一路树的node作为独特的uid
#如果是空的就返回*号，然后对比如果在path这个defaultdict
#出现过的话就加进去答案里面。
#一个root = [1,2,3,4,null,2,4,null,null,4]
#寻找path的uid轨迹是这样的:
#4**
#24***
#4**
#24***
#4**
#324***4**
#124***324***4**