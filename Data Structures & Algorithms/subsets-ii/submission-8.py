class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        nums.sort()
        n = len(nums)
        def subsets(i):
            if i > len(nums):
                return
            
            res.append(curr.copy())
            for j in range(i, n):
                # if duplicate
                if j >i and nums[j]==nums[j-1]:
                    continue

                curr.append(nums[j])        
                subsets(j+1)
                curr.pop()
            
        subsets(0)
        return res
