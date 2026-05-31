class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxTotal = nums[0]
        accumulated = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            accumulated += num
            if num >= accumulated:
                accumulated = num
            maxTotal = max(accumulated, maxTotal)
        
        return maxTotal