class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjacencyList = {}

        visited = set()


        def dfs(prev, curr):

            if curr in visited:
                return True

            visited.add(curr)
            
            for neighbor in adjacencyList[curr]:
                if neighbor != prev:
                    if dfs(curr, neighbor):
                        return True
            
            return False



        setOfEdges = set()

        for u,v in edges:
            if u not in adjacencyList:
                adjacencyList[u] = []
            if v not in adjacencyList:
                adjacencyList[v] = []
            adjacencyList[v].append(u)
            adjacencyList[u].append(v)

            visited.clear()
            
            if dfs(-1, u):
                return [u, v]
            
        return []



