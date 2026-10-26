class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr):
            # largest # <= target
            l,r = 0, len(arr)-1
            while l < r:
                m = (l + r + 1) // 2
                if arr[m] < target:
                    l = m
                elif arr[m] > target:
                    r = m - 1
                else:
                    return m
            
            return l

        rows = [matrix[r][0] for r in range(len(matrix))]
        r = binary_search(rows) # search for which row contains element
        cols = matrix[r]

        c = binary_search(cols)
        return matrix[r][c] == target
