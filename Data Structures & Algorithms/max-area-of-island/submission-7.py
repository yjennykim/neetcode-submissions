from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        neighbors = [[-1,0], [1,0], [0,-1], [0,1]]        

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            area = 1

            while q:
                x,y = q.popleft()

                for i,j in neighbors:
                    if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]) and grid[x+i][y+j] == 1:
                        q.append((x+i, y+j))
                        grid[x+i][y+j] = 0
                        area += 1
            
            return area

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    max_area = max(area, max_area)
        
        return max_area
