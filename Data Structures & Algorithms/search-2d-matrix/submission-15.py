class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = [matrix[i][0] for i in range(len(matrix))]

        # Last L <= target
        l,r = 0, len(rows)-1
        while l < r:
            m = (l + r + 1) // 2
            if rows[m] <= target:
                l = m # keep candidacy
            else: 
                r = m - 1
        
        row = matrix[l]
        l,r = 0, len(row)-1
        while l <= r:
            m = (l + r) // 2
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else: 
                return True
        
        return False