class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # [1,2,1]
        # [], [1], [1,2], [1,2,1], [2], [1,1]

        curr = []
        res = []
        nums.sort()
        # [1,1,2]

        def subsets(index):
            if index > len(nums):
                return
            
            
            res.append(curr.copy())
            for j in range(index, len(nums)):
                # if duplicate
                if j>index and nums[j]==nums[j-1]:
                    continue
                curr.append(nums[j])        
                subsets(j+1)
                curr.pop()
            
    
        subsets(0)

        return res
