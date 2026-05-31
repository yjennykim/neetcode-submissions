class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        maxProd = res = minProd = nums[0]

        for i in range(1, len(nums)):
            currNum = nums[i]
            temp = maxProd * currNum
            maxProd = max(currNum, maxProd * currNum, minProd * currNum)
            minProd = min(currNum, temp, minProd * currNum)
            res = max(maxProd, res)
            

        return res