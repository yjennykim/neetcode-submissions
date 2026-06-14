class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        while l < r:
            m = (l + r + 1) // 2
            if arr[m] <= x:
                l = m
            else:
                r = m - 1
        
        if l < len(arr)-1 and abs(x - (arr[l+1])) < abs(x - (arr[l])):
            l += 1

        r = l
        while r-l+1 < k:
            if r == len(arr) - 1:
                l -= 1
            elif l == 0:
                r += 1
            elif abs(arr[r+1] - x) < abs(arr[l-1] - x):
                r += 1
            else:
                l -= 1
        
        return arr[l:r+1]