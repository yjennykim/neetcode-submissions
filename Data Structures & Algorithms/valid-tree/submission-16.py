from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        adjacencyList = {}

        for n1, n2 in edges:
            print(n1, n2)
            if n1 == n2:
                return False 

            if n1 not in adjacencyList:
                adjacencyList[n1] = set()
            if n2 not in adjacencyList:
                adjacencyList[n2] = set()
            adjacencyList[n1].add(n2)
            adjacencyList[n2].add(n1)

        # no edges
        if n == 1:
            return True
            
        print('adjacecylist', adjacencyList)

        startingNode = edges[0][0]
        prev = -1
        q = deque()
        visited = set()
        
        q.append((prev,startingNode))
        visited.add(startingNode)

        while q:
            prev, node = q.popleft()
            for neighbor in adjacencyList[node]:
                if neighbor == prev:
                    continue

                if neighbor in visited :
                    return False

                q.append((node,neighbor))
                visited.add(neighbor)
        
        if len(visited) == n:
            return True
        
        return False


        
