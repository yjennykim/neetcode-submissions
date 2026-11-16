class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        targets = [0] * (target + 1)
        # base cases
        for num in nums:
            if num <= target:
                targets[num] = 1

        for i in range(target + 1):
            for num in nums:
                if num < i:
                    targets[i] += targets[i - num]
        
        return targets[target]