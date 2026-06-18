class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        new = set()
        for i in range(n):
            graph[i] = []
            new.add(i)

        # build out adjacency graph
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            # seen before
            if node not in new:
                return False
            
            new.remove(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node): 
                        return False

            return True

        if not dfs(0, -1): return False

        # unseen set
        if len(new) > 0:
            return False
        
        return True

            
        # look for cycles, use visited for new connected component
        
