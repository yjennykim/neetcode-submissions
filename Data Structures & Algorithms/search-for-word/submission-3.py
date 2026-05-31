class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        # index at word
        def recurse(x, y, index):
            # cat -> index 3 means all characters have been found
            if index == len(word):
                return True

            if (x,y) in visited:
                return False

            # out of bounds e.g. y >= 4
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                
                return False

            visited.add((x,y))

            found = (
                board[x][y] == word[index] 
                and (recurse(x+1, y, index+1)
                or recurse(x-1, y, index+1)
                or recurse(x, y+1, index+1)
                or recurse(x, y-1, index+1))     
            ) 
            if not found:
                visited.remove((x, y))
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if recurse(i,j,0): 
                        return True
                    # visited.clear()
        
        return False
        

            

