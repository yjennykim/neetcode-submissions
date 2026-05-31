class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        dp = [False] * (target + 1)

        if total % 2 != 0: return False    


        
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]

        """
        2, 2, 3, 5

        F, F, F, F, F, F
        F, T, T, F, T, F
        X, T, 

        """
        




