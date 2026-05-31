class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]

        def dfs(wordIndex, i,j):
            if wordIndex == len(word):
                return True

            if i >= len(board) or i < 0 or j < 0 or j >= len(board[0]) or word[wordIndex] != board[i][j]:
                return False
            
            visited.add((i,j))
            for x,y in dirs:
                if (i+x, y+j) not in visited:
                    if dfs(wordIndex+1, i+x, y+j):
                        return True

            visited.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0,i,j):
                        return True
        
        return False
        
