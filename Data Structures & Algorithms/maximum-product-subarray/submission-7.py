class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = maxProd = minProd = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            temp = maxProd
            maxProd = max(curr, maxProd * curr, minProd * curr)
            minProd = min(curr, temp * curr, minProd * curr)
            res = max(maxProd, res)
        return res