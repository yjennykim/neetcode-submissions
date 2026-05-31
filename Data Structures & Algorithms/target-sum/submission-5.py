class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        
        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            # index to explore next, current total
            current_ways = 0
            current_ways += dfs(i + 1, total + nums[i])
            current_ways += dfs(i + 1, total - nums[i])

            return current_ways

        
        return dfs(0, 0)
