from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = {}
        for i in range(n):
            adjacencyList[i] = []

        for a, b in edges:
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)

        # if n == 0: return 0
        # if n == 1: return 1

        q = deque()
        seen = [False] * n
        q.append(0)
        seen[0] = True

        connected = 0
        while n != 0:
            connected += 1

            while q:
                node = q.popleft()
                n -= 1

                for neighbor in adjacencyList[node]:
                    if not seen[neighbor]:
                        q.append(neighbor)
                        seen[neighbor] = True

            for i in adjacencyList.keys():
                if not seen[i]:
                    seen[i] = True
                    q.append(i)
                    break
        print("Conencted", connected)
        return connected