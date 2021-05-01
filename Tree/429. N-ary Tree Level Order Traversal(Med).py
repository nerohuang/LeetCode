"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        store = [root];
        level = [];
        while store:
            lenght = len(store);
            newStore = [];
            curLevel = [];
            for i in range(lenght):
                node = store.pop(0);
                curLevel.append(node.val);
                if node.children:
                    for child in node.children:
                        newStore.append(child);
            level.append(curLevel);
            store = newStore;
        return level

#bfs