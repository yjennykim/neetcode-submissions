class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        L = window = 0
        for R in range(len(nums)):
            window += nums[R]

            while window >= target:
                min_length = min(min_length, R - L + 1)
                window -= nums[L]
                L += 1
        
        if min_length == float('inf'):
            return 0

        return min_length