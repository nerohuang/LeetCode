"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        self.ans  = 0
        
        def find(root, count, ans):
            if not root:
                return
            self.ans = max(count, self.ans );
            for child in root.children:
                find(child, count + 1, self.ans);
        
        find(root, 1, self.ans)
        
        return self.ans 

