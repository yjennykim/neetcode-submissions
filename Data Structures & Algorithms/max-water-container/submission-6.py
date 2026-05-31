class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mmax = 0

        l, r = 0, len(heights)-1

        while l < r:
            mmax = max(min(heights[l], heights[r]) * (r-l), mmax)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return mmax