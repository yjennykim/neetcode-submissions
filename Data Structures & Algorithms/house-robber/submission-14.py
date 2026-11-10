class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        best = [0] * n

        # base cases
        if n == 0: return 0
        if n == 1: return nums[0]

        best[0] = nums[0]
        best[1] = max(nums[1], nums[0])

        for i in range(2, n):
            # rob two houses down and this one OR rob the house next door
            best[i] = max(best[i-2] + nums[i], best[i-1])
        
        return best[n-1]