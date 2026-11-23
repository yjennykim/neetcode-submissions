from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(curr: List[int], i: int) -> None:
            if i == len(nums):
                ans.append(curr.copy())
                return

            # 1. Include nums[i]
            curr.append(nums[i])
            dfs(curr, i + 1)
            curr.pop()

            # 2. Exclude nums[i] and skip all duplicates of nums[i]
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1
            dfs(curr, next_i)

        dfs([], 0)
        return ans