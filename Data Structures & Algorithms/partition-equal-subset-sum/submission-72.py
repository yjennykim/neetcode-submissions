class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        target = sum(nums) // 2
        # reject trying to sum up to floating #
        if total % 2 != 0: 
            return False

        # dp[i] = subset adding up to dp[i] exists
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num-1, -1):
                if dp[j - num]:
                    dp[j] = True
                
        return dp[target]
                 