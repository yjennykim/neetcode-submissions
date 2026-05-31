"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        # initialize queue of nodes to process
        q = deque()
        q.append(node)
        
        # mapping node -> copy
        mapping = {}
        processed = set()

        # while q is not empty, process node and neighbors
        while q:
            nodeToCopy = q.popleft()
            curr = Node(nodeToCopy.val) if nodeToCopy not in mapping else mapping[nodeToCopy]

            for neighbor in nodeToCopy.neighbors:
                neighborCopy = None
                if neighbor not in mapping:
                    neighborCopy = Node(neighbor.val)
                    mapping[neighbor] = neighborCopy
                else:
                    neighborCopy = mapping[neighbor]

                print(f"Setting neighbor {neighbor.val}")
                curr.neighbors.append(neighborCopy)

                # append to queue to process neighbors    
                if neighbor not in processed:
                    processed.add(neighbor)
                    q.append(neighbor)
            
            mapping[nodeToCopy] = curr
            processed.add(nodeToCopy)

        # return first node
        return mapping[node]
