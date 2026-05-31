from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        islandCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    q = deque()
                    q.append((i,j))
                    
                    # bfs from this point
                    while q:
                        i,j = q.popleft()
                        grid[i][j] = "0"

                        for x,y in dirs:
                            # within bounds
                            if 0<=i+x<len(grid) and 0<=j+y<len(grid[0]) and grid[i+x][y+j]=="1":
                                q.append((i+x, y+j))

                    islandCount += 1
        
        return islandCount
                







