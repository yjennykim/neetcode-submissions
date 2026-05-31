class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(current, remaining):
            if not remaining:
                result.append(current)
                return
            for i in range(len(remaining)):
                # Choose the current number and explore further
                backtrack(current + [remaining[i]], remaining[:i] + remaining[i+1:])
    
        backtrack([], nums)
        return result
            