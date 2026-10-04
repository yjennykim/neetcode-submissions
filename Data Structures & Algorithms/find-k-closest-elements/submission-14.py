class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        R = len(arr) - k
        
        while L < R:
            M = (L + R) // 2
            
            # Compare the distance from x to arr[M] vs arr[M + k]
            # If x is closer to arr[M + k], our window needs to shift right.
            if x - arr[M] > arr[M + k] - x:
                L = M + 1
            else:
                R = M
                
        return arr[L : L + k]