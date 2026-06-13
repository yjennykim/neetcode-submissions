class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize window ptrs, global counter
        # Start shrinking window as soon as >= target
        if len(nums) == 0:
            return 0

        l,r = 0,0
        running = 0
        min_total = len(nums) + 1
        while r < len(nums):
            running += nums[r]
            while running >= target:
                min_total = min(r-l+1, min_total)
                running -= nums[l]
                l += 1
            r += 1
        if min_total == len(nums) + 1:
            return 0
        return min_total
            

