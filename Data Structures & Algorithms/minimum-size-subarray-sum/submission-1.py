class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums)
        L = window = 0
        for R in range(len(nums)):
            window += nums[R]

            while window >= target:
                min_length = min(min_length, R - L + 1)
                window -= nums[L]
                L += 1
        
        if R-L+1 == len(nums) and window < target:
            return 0

        return min_length