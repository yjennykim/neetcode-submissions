class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)
        maxLength = 1

        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i, -1, -1):
                prev = nums[j]
                if curr > prev:
                    lengths[i] = max(lengths[i], lengths[j] + 1)
            
            maxLength = max(lengths[i], maxLength)
        
        return maxLength