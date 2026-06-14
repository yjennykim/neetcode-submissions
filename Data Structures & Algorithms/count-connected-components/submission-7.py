from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initialize counter, adj list
        # create a visited set

        # for each node
            # if not in visited set:   
                # increment # connected component
                # DFS
        def bfs(start, visited):
            q = deque()
            visited.add(start)
            q.append(start)

            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited and neighbor != node:
                        visited.add(neighbor)
                        q.append(neighbor)
        
        def dfs(node, visited):
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor != node:
                    visited.add(neighbor)
                    dfs(neighbor, visited)

        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        connected = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                connected += 1
                dfs(i, visited) 
        
        return connected
        
