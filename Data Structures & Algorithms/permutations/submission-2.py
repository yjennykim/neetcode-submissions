class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        ans = [] 
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            
            for i, num in enumerate(nums):
                if not visited[i]:
                    visited[i] = True
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
                    visited[i] = False
            
        backtrack([])
        return ans