from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = {}
        visted = set()
        q = deque()
    
        for i in range(n): graph[i] = []

        # build out adjacency graph
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q.append(0)
        visted.add(0)
        while q:
            start = q.popleft()        
            for neighbor in graph[start]:
                if neighbor not in visted:
                    q.append(neighbor)
                    visted.add(neighbor)
        
        if len(visted) != n: 
            return False
        
        return True