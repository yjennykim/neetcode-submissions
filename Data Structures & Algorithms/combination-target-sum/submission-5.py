class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(i, curr, total):    
            if total == target:
                ans.append(curr.copy())
                return

            if total > target:
                return

            # dfs(i+1, curr, total)
            # curr.append(nums[i])
            # dfs(i+1, curr, total + nums[i])
            # curr.pop()
            
            for j in range(i,len(nums)):
                curr.append(nums[j])
                dfs(j, curr, total + nums[j])
                curr.pop()

        dfs(0, [], 0)
        return ans