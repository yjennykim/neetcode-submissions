class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums) - 1
        for l in range(len(nums)-1, -1, -1):
            skipCount = nums[l]
            if l + skipCount >= r:
                r = l
        
        return r == 0