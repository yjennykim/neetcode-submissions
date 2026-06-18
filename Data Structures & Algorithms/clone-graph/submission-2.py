"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        # second pass, assign neighbors
        store = {}
        def dfs(root):
            if not root:
                return
            
            store[root] = Node(root.val)
            for neighbor in root.neighbors:
                if neighbor not in store:
                    dfs(neighbor)
        
        visited = set()
        def dfs2(root):
            if not root: 
                return
            
            copy = store[root]
            visited.add(root.val)

            for neighbor in root.neighbors:
                copy.neighbors.append(
                    store[neighbor]
                )
                if neighbor.val not in visited:
                    dfs2(neighbor)

        # one pass, store refs orig -> copied node
        dfs(node)
        dfs2(node)

        return store[node]

