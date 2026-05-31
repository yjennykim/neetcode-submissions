class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        if sum(nums) % 2 != 0:
            return False
        dp[0] = True # can def add up to 0 
        
        for num in nums:
            for j in range(target, num-1, -1):
                    dp[j] = dp[j] or dp[j-num]
        
        return dp[target]
                