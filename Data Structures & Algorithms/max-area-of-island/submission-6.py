from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:      
        maxArea = 0
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]

        # returns area of island
        def bfs(i,j):
            q = deque()
            q.append((i,j))

            currArea = 0

            while q:
                x,y = q.popleft()
                # mark as visited
                print("Popped", x, y)
                grid[x][y] = 0
                currArea += 1

                for dx,dy in dirs:
                    if 0<=dx+x<len(grid) and 0<=dy+y<len(grid[0]) and grid[dx+x][dy+y]==1:
                        # mark as visited
                        grid[dx+x][dy+y] = 0
                        q.append((dx+x, dy+y))
            
            return currArea
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    print("Starting BFS on", i, j)
                    currArea = bfs(i,j)
                    print(f"area {currArea}")
                    # start BFS
                    maxArea = max(maxArea, currArea)
        
        return maxArea
                    






        