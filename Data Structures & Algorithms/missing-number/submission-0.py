class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumN = (n * (n+1)) // 2

        print(sumN)
        return sumN - sum(nums)