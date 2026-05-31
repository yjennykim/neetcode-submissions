class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        candidates.sort()
        def recurse(total, index):
            if total > target:
                return
            
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(index, len(candidates)):
                if j > index and candidates[j] == candidates[j - 1]:
                    continue
                curr.append(candidates[j])
                recurse(total + candidates[j], j+1)
                curr.pop()
        
        recurse(0, 0)
        return res

