class Solution:
    def streetRob(self, nums):
        dp = [0] * len(nums)
        
        # base case
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]


    def rob(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)

        street1 = nums[1:]
        street2 = nums[:len(nums)-1]

        best1 = self.streetRob(street1)
        best2 = self.streetRob(street2)

        return max(best1, best2)



