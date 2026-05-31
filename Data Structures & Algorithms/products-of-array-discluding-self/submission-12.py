class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,4,6]
        '''
        res = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i != j:
                    total *= nums[j]
            res.append(total)
        return res
