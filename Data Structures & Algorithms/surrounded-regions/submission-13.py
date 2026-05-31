from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # if O on edge, then cannot be surrounded
        
        """
            Approach: 
                - Find O's on the border
                - Add to Queue to process
                - BFS inwards to find all the O's connected to it, mark as visited by changing to 'V'

                - At the end, traverse grid, revert 'V' -> 'O' and 'O' -> 'X'
        """
        q = deque()

        # add border "O"
        for r in range(len(board)):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][len(board[0])-1] == "O":
                q.append((r, len(board[0])-1))

        # r, c
        for c in range(len(board[0])):
            if board[0][c] == "O":
                q.append((0,c))
            if board[len(board)-1][c] == "O":
                q.append((len(board)-1, c))
        
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        while q:
            i,j = q.popleft()
            board[i][j] = "V"

            for x,y in dirs:
                if 0<=x+i<len(board) and 0<=y+j<len(board[0]) and board[x+i][y+j] == "O":
                    board[x+i][y+j] = "V"
                    q.append((x+i, y+j))
            
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "V":
                    board[i][j] = "O"


                    


