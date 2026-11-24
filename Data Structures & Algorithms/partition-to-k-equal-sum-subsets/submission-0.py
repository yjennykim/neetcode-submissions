class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        used = [False] * len(nums)

        def generate(running, i, subsets_left):
            if subsets_left == 0: 
                return True

            if running > target:
                return False
            
            if running == target:
                # found 1 subset, try find next subset
                return generate(0, 0, subsets_left - 1)
            
            for j in range(i, len(nums)):
                if used[j]:
                    continue
                
                used[j] = True
                if generate(running + nums[j], j + 1, subsets_left):
                    return True
                used[j] = False
            
            return False

        return generate(0, 0, k)