class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Extract the first column elements
        cols = [row[0] for row in matrix]
        
        l, r = 0, len(cols) - 1
        while l <= r:  # Keep l <= r to include all indices
            m = (l + r) // 2
            if cols[m] < target:
                l = m + 1  # Search in the right half
            elif cols[m] > target:
                r = m - 1  # Search in the left half
            else:
                return True  # Found the exact target

        # After the loop, l points to the first element greater than target
        # Therefore, r points to the largest element less than or equal to target
        row_index = r
        
        if row_index < 0:  # If row_index is out of bounds
            return False
        
        row = matrix[row_index]
        
        # Binary search in the identified row
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True
        
        return False