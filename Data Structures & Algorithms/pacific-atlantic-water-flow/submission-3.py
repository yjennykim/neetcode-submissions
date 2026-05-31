from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # initialize a q, visited set, results list
        q = deque()

        # find pacific + atlantic border cells, insert into q
        is_reachable_pacific = set()
        is_reachable_atlantic = set()
        for r in range(len(heights)):
            is_reachable_pacific.add((r,0))
            is_reachable_atlantic.add((r, len(heights[0])-1))
            q.append((r,0))

        for c in range(len(heights[0])):
            is_reachable_pacific.add((0,c))
            is_reachable_atlantic.add((len(heights)-1, c))
            q.append((0,c))
        
        print(f"Atlantic {is_reachable_atlantic}")
        print(f"Pacific {is_reachable_pacific}")

        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        def bfs(visited_set):
            while q:
                i,j = q.pop()
                curr_height = heights[i][j]

                # check all directions, add to visited, and q
                for x,y in dirs:
                    neighbor = ((x+i, y+j))

                    if 0<=x+i<len(heights) and 0<=y+j<len(heights[0]) and neighbor not in visited_set and curr_height <= heights[x+i][y+j]:
                        visited_set.add(neighbor)
                        q.append(neighbor)

        bfs(is_reachable_pacific)

        for i,j in list(is_reachable_atlantic):
            q.append((i,j))
        
        bfs(is_reachable_atlantic)
        common_cells = is_reachable_pacific.intersection(is_reachable_atlantic)

        return list(common_cells)

                    

             