class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def recurse(total, index):
            if total > target:
                return
            
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(index, len(nums)):
                curr.append(nums[j])
                recurse(total+nums[j], j)
                curr.pop()
        
        recurse(0, 0)
        return res
