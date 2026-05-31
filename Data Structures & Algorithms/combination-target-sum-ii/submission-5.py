class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        def dfs(i, total, curr):
            if total > target:
                return
            
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                # j and i are indices within candidates... if we're looking at the same number again
                # candidates = [1, 1, 2, 2, 3], target = 4
                                                                
                if j == i or candidates[j] != candidates[j-1]:
                    curr.append(candidates[j])
                    dfs(j+1, total + candidates[j], curr)
                    curr.pop()

        
        dfs(0, 0, [])
        return res