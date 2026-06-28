from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))

        neighbors = [[-1,0], [1,0], [0,1], [0,-1]]
        while q:
            r,c = q.popleft()
            visited.add((r,c))

            for x,y in neighbors:
                if 0<=x+r<len(grid) and 0<=y+c<len(grid[0]) and grid[x+r][y+c]!=-1 and (x+r, y+c) not in visited:
                    visited.add((x+r, y+c))
                    q.append((x+r, y+c))
                    grid[x+r][y+c] = grid[r][c] + 1
            