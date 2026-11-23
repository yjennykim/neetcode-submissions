class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def dfs(curr, running, i):
            if running == target:
                ans.append(curr.copy())
                return
            
            if running > target:
                return
            
            for j in range(i,n):
                if candidates[j-1] == candidates[j] and i != j:
                    continue
                curr.append(candidates[j])
                dfs(curr, running + candidates[j], j + 1)
                curr.pop()
        
        dfs([], 0, 0)
        return ans