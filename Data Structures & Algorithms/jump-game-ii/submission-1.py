class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # No jumps needed if there's only one element
        
        # Initialize minSteps array with infinity values
        minSteps = [math.inf] * n
        minSteps[n - 1] = 0  # No steps needed to reach the last index

        for i in range(n - 2, -1, -1):
            maxJump = min(i + nums[i], n - 1)  # Max index we can jump to from index i
            for j in range(i + 1, maxJump + 1):  # Check jumps from i to the max possible index
                minSteps[i] = min(minSteps[i], minSteps[j] + 1)
        
        return minSteps[0]

