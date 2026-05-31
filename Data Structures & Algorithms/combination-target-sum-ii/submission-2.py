class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        def dfs(i, total, curr):
            if total > target:
                return
            
            if total == target and curr not in res:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):

                curr.append(candidates[j])
                dfs(j+1, total + candidates[j], curr)
                curr.pop()

        
        dfs(0, 0, [])
        return res