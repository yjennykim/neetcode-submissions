class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
        
        def recurse(index):
            if index > len(nums):
                return

            res.append(curr.copy())

            for j in range(index, len(nums)):
                if j > index and nums[j] == nums[j - 1]:
                    continue

                curr.append(nums[j])
                recurse(j + 1)
                curr.pop()

        
        recurse(0)
        return res
