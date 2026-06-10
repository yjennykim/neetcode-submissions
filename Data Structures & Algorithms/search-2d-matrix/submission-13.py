class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search for correct row
        rows = [matrix[i][0] for i in range(len(matrix))]

        # Search for biggest L < target
        l, r = 0, len(matrix)-1
        while l < r: 
            m = (l + r + 1) // 2
            if rows[m] > target:
                # too big, remove from candidacy
                r = m - 1
            else:
                # too small, keep as option
                l = m
        
        if rows[l] == target:
            return True
        
        rows = matrix[l]
        l, r = 0, len(rows) - 1
        while l <= r:
            m = (l + r) // 2
            if rows[m] > target:
                r = m - 1
            elif rows[m] < target:
                l = m + 1
            else:
                return True
        
        return False