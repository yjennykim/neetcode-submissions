class Solution:
    def rob(self, nums: List[int]) -> int:

        def houseRobber(subNums):
            if len(subNums) == 0: return 0
            if len(subNums) == 1: return subNums[0]
            if len(subNums) == 2: return max(subNums)
            
            OPT = [0] * len(subNums)
            OPT[0] = subNums[0]
            OPT[1] = max(subNums[0], subNums[1])

            for i in range(2, len(subNums)):
                OPT[i] = max(OPT[i-1], OPT[i-2] + subNums[i])
                
            return OPT[-1]
        
        if len(nums) == 1:
            return nums[0]
        return max(
            houseRobber(nums[1:]), 
            houseRobber(nums[:-1])
        )