import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k > len(arr):
            return []

        # 1. Safely find the closest starting index using binary search
        idx = bisect.bisect_left(arr, x)
        
        # Handle edge cases where x is outside or at the bounds of the array
        if idx == 0:
            L = R = 0
        elif idx == len(arr):
            L = R = len(arr) - 1
        else:
            # Pick the closer of the two surrounding elements
            if abs(arr[idx] - x) < abs(arr[idx - 1] - x):
                L = R = idx
            else:
                L = R = idx - 1

        # 2. Your expansion loop (grows the window until it has k elements)
        for i in range(k - 1):
            if L - 1 < 0:
                R += 1
            elif R + 1 >= len(arr):
                L -= 1
            elif abs(x - arr[L - 1]) <= abs(x - arr[R + 1]):
                L -= 1  # Prefer smaller elements on ties
            else: 
                R += 1
        
        return arr[L : R + 1]