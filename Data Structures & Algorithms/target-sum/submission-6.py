class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        
        def dfs(i, total):
            
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            if (i, total) in self.memo:
                return self.memo[(i, total)]

            current_ways = 0
            current_ways += dfs(i + 1, total + nums[i])
            current_ways += dfs(i + 1, total - nums[i])
            self.memo[(i, total)] = current_ways
            return current_ways

        return dfs(0, 0)
