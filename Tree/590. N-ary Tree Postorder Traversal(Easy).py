"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = [];
        
        def post(node):
            if not node:
                return
            if node and node.children:
                for child in node.children:
                    post(child);
            ans.append(node.val);
        
        post(root);
        
        return ans;