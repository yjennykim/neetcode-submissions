class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = []
        for r in matrix:
            rows.append(r[0])

        l, r = 0, len(rows)-1
        while l < r:
            # biggest number < target
            m = (l + r + 1) // 2
            if rows[m] > target:
                r = m - 1
            elif rows[m] < target:
                l = m 
            else:
                return True
        
        target_row = matrix[l]
        
        l, r = 0, len(target_row)-1
        while l <= r:
            m = (l + r) // 2
            if target_row[m] > target:
                r = m - 1
            elif target_row[m] < target:
                l = m + 1
            else: 
                return True
    
        return False
 

