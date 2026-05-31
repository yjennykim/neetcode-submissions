class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        # OPT[i] = max(OPT[i-2] + nums[i], OPT[i-1]) 
        OPT = [0] * len(nums)
        OPT[0] = nums[0]
        OPT[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            OPT[i] = max(OPT[i-2] + nums[i], OPT[i-1])
        
        return max(OPT[len(nums)-1], OPT[len(nums)-2])
