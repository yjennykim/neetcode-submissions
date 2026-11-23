class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(wordIdx,i,j):
            if wordIdx >= len(word):
                return True
            temp = board[i][j]
            board[i][j] = "#"  
            for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
                dx,dy = x+i, y+j
                if 0 <= dx < len(board) and 0 <= dy < len(board[0]) and board[dx][dy] == word[wordIdx]:
                    if dfs(wordIdx + 1, dx, dy):
                        return True
            board[i][j] = temp
                
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(1,i,j): return True
        
        return False
        
                

            
            
        