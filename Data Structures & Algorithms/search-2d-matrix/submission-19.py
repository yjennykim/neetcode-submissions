class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        l,r = 0, num_rows * num_cols - 1

        while l <= r:
            m = (l + r) // 2
            row = m // num_cols
            col = m % num_cols

            val = matrix[row][col] 
            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return True
            
        return False
        

                
