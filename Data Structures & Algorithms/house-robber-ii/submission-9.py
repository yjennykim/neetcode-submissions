class Solution:
    def rob(self, nums: List[int]) -> int:

        def houseRobber(subNums):
            if len(subNums) == 0:
                return 0
            if len(subNums) == 1:
                return subNums[0]
            if len(subNums) == 2:
                return max(subNums)
            
            OPT = [0] * len(subNums)  # Create an array to store max rob amount at each house
            OPT[0] = subNums[0]  # For the first house, the only option is to rob it
            OPT[1] = max(subNums[0], subNums[1])  # For the second house, take the max of the first two houses

            for i in range(2, len(subNums)):
                # For each house, choose either to rob it and add the previous non-adjacent house's value
                # or skip it and take the value from the previous house
                OPT[i] = max(OPT[i-1], OPT[i-2] + subNums[i])

            return OPT[-1]  # Return the result from the last house
        
        # Two cases: rob from house 1 to the last or rob from house 0 to the second-to-last
        if len(nums) == 1:
            return nums[0]
        return max(
            houseRobber(nums[1:]),  # Rob houses from 1 to the end
            houseRobber(nums[:-1])  # Rob houses from 0 to the second-to-last
        )
