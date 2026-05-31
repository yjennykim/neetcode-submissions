class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ways = 0

        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    self.ways += 1
                return

            # index to explore next, current total
            dfs(i + 1, total + nums[i])
            dfs(i + 1, total - nums[i])

        
        dfs(0, 0)
        return self.ways

        """
            (0, 0) -> invoke dfs(1, 2), dfs(1, -2)
            (1,2) -> invoke dfs(2, 4), dfs(2, 0)        (1,-2) -> invoke dfs(2, 0), dfs(2, -4)
            (2,4) -> invoke  dfs(3,6), dfs(3,2)  
            (2,0) -> invoke dfs(3,2), dfs(3,-2)
            (2,-4) -> invoke dfs(3,-2), dfs(3,-6)
            (2, 0) -> invoke dfs(3,2), dfs(3,-2)
            
        """