from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    q.append((i,j))

                    while q:
                        x,y = q.popleft()
                        grid[x][y] = '0'

                        for a,b in [[-1,0], [0,1], [1,0], [0,-1]]:
                            if 0 <= x+a < len(grid) and 0 <= y+b < len(grid[0]) and grid[x+a][y+b] == '1':
                                q.append((x+a, y+b))
                    
                    islands += 1

        return islands 
        
                    
