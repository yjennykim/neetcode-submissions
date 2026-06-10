class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Look for where nums[i] > nums[i+1]
        
        # Get midpoint, compare to L, R
        # If M < R: that portion is sorted
        # If L < M: that portion is sorted
        # Want to explore unsorted list

        # Find biggest num, put it at L
        l,r = 0, len(nums)-1

        while l < r: 
            m = (l + r + 1) // 2

            if nums[m] > nums[l]:
                l = m
            # left side is unsorted
            else:
                r = m - 1
        
        if l == len(nums)-1:
            return nums[0]
        
        return nums[l+1]
        
