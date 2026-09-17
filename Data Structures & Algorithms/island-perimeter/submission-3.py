class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        neighbors = [[-1,0], [1,0], [0,1], [0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for x,y in neighbors:
                        if x+i < 0 or y+j < 0 or x+i >= len(grid) or y+j >= len(grid[0]) or grid[x+i][y+j] == 0:
                            perim += 1
                         
        return perim