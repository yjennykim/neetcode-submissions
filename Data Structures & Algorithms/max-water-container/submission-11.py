class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Always prefer to keep biggest, lower i

        l,r = 0,len(heights)-1 # start with ends, in order to maximize for width variable
        max_volume = 0

        while l < r:
            volume = min(heights[l], heights[r]) * (r-l)
            max_volume = max(volume, max_volume)
            # keep highest bar
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_volume
