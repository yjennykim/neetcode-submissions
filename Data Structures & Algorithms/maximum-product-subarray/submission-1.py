class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxProduct = res = minProduct = nums[0]

        for r in range(1,len(nums)):
            currNum = nums[r]
            temp = maxProduct * currNum
            maxProduct = max(currNum, maxProduct * currNum, minProduct * currNum)
            minProduct = min(currNum, temp, minProduct * currNum)
            res = max(maxProduct, res)
        
        return res

