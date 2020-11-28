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

#和116一样，改都不用改，因为BFS的存储方式可以省略掉缺失的node。
