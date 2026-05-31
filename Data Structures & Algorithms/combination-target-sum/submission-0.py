class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def recurse(i, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            
            if currSum > target:
                return
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                recurse(j, currSum + nums[j])
                curr.pop()

        
        recurse(0, 0)
        return res


