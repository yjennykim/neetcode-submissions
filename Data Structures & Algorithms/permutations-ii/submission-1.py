class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        ans = []
        nums.sort()

        def backtrack(curr: List[int]):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for j, num in enumerate(nums):
                if visited[j]:
                    continue
                
                if j > 0 and nums[j] == nums[j-1] and visited[j-1]:
                    continue

                visited[j] = True
                curr.append(num)
                backtrack(curr)
                curr.pop()
                visited[j] = False

        backtrack([])
        return ans