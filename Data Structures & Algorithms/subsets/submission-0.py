class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []
        def recurse(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            recurse(i+1)
            curr.pop()
            recurse(i+1)
        
        recurse(0)
        return res
            