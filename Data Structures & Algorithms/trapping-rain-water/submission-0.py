class Solution:
    def trap(self, height: List[int]) -> int:
        # water[i] = min(height[i-1], height[i+1]) - height[i]
        if not height:
            return 0

        n = len(height)
        maxLeft = [0] * n 
        maxRight = [0] * n
        minLeftAndRight = [0] * n

        max_so_far = 0
        for i in range(n):
           max_so_far = max(max_so_far, height[i])
           maxLeft[i] = max_so_far

        max_so_far = 0        
        for i in range(n):
            end = len(height) - 1 - i
            max_so_far = max(max_so_far, height[end])
            maxRight[end] = max_so_far
            
        for i in range(n):
            minLeftAndRight[i] = min(maxLeft[i], maxRight[i])
        
        sum_water = 0
        for i in range(n):
            sum_water += max(0, minLeftAndRight[i] - height[i])
        
        return sum_water
