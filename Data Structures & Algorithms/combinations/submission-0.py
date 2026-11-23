class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(curr: List, i: int):
            if len(curr) == k:
                ans.append(curr.copy())
                return

            for j in range(i, n+1):
                curr.append(j)
                dfs(curr, j+1)
                curr.pop()
        
        dfs([], 1)
        return ans

