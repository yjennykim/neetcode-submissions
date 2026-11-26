class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = 0, len(arr)-1

        while R-L+1 > k:
            if abs(x - arr[L]) <= abs(x - arr[R]): # left is closer in case of tie
                R -= 1
            else:
                L += 1
        
        return arr[L:R+1]