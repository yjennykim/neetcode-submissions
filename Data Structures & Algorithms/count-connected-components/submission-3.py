from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = {}
        for i in range(n):
            adjacencyList[i] = []

        for a, b in edges:
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)

        seen = [False] * n

        connected = 0

        def bfs(i):
            q = deque([i])
            seen[i] = True

            while q:
                node = q.popleft()

                for neighbor in adjacencyList[node]:
                    if not seen[neighbor]:
                        q.append(neighbor)
                        seen[neighbor] = True

        
        for i in range(n):
            if not seen[i]:
                bfs(i)
                connected += 1
        
        return connected