
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        # find all the treasure chests
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    # call bfs on each treasure chest
                    q.append((i,j))        
    
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        visited = set()

        # while loop to continue as long as queue is not empty
        while q:
            i,j = q.popleft()
            visited.add((i,j))

            # check neighbors in each direction, inc counters
            for dx,dy in dirs:
                # within bounds
                if 0<=dx+i<len(grid) and 0<=dy+j<len(grid[0]) and grid[dx+i][dy+j] != -1 and (dx+i, dy+j) not in visited:
                    q.append((dx+i, dy+j))
                    visited.add((dx+i, dy+j))
                    grid[dx+i][dy+j] = grid[i][j] + 1
        
        
