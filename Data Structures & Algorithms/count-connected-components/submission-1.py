from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = {}
        for i in range(n):
            adjacencyList[i] = []

        for a, b in edges:
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)

        if n == 0: return 0
        if n == 1: return 1

        q = deque()
        seen = set()
        q.append(0)
        seen.add(0)

        connected = 0
        while n != 0:
            connected += 1

            while q:
                node = q.popleft()
                n -= 1

                for neighbor in adjacencyList[node]:
                    if neighbor not in seen:
                        q.append(neighbor)
                        seen.add(neighbor)

            for i in adjacencyList.keys():
                if i not in seen:
                    print("appending", i)
                    seen.add(i)
                    q.append(i)
                    break
        print("Conencted", connected)
        return connected