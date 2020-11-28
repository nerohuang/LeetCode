"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None;
        
        store = [];
        store.append(root);
        
        while store:
            for i in range(1, len(store)):
                store[i - 1].next = store[i];
            store[-1].next = None;
            nextLevel = [];
            for node in store:
                if node.left:
                    nextLevel.append(node.left);
                if node.right:
                    nextLevel.append(node.right);
            store = nextLevel;
        
        return root

#思路：用BFS：
#然后因为BFS的原理天然的就会把同一深度的node全部存起来
#然后只要在深度交替之前将这些存好的node for一遍
#然后i的next是i + 1. 当最后一个next是None就可以了。