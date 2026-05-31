class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]

        visited = set()
        def dfs(wordIndex, i, j):
            if wordIndex == len(word):
                return True
            
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != word[wordIndex]:
                return False
        
            visited.add((i,j))
            for x,y in dirs:
                if (i+x,j+y) not in visited:
                    if dfs(wordIndex + 1, i+x, j+y):
                        return True
                    
            visited.remove((i,j))
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True

        return False