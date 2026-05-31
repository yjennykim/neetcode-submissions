from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshFruitRemaining = 0
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]

        # search for rotten fruits, add to queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    freshFruitRemaining += 1
                    
        # start timer
        minute = 0

        # while q is not empty:
        while q:
            # pop from queue
            i,j,currMin = q.popleft()
            minute = max(currMin, minute)
            
            # explore neighbors, check for fresh fruit (1), mark as rotten, add to new queue
            for x,y in dirs:
                if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]) and grid[x+i][y+j] == 1:
                    grid[x+i][y+j] = 2
                    freshFruitRemaining -= 1
                    q.append((x+i, y+j, currMin+1))
        
        if freshFruitRemaining > 0:
            return -1
            
        # return timer
        return minute
        

        """
        1 0 1
        0 2 0 
        1 0 1
        """


