class Solution:
    def rob(self, nums: List[int]) -> int:
        OPT = [0] * len(nums)
        OPT[0] = nums[0]
        if len(nums) == 1: return OPT[0]

        OPT[1] = max(nums[0], nums[1])
        if len(nums) == 2: return OPT[1]

        for i in range(2, len(nums)):
            OPT[i] = max(OPT[i-2] + nums[i], OPT[i-1])
        
        return OPT[len(nums)-1]