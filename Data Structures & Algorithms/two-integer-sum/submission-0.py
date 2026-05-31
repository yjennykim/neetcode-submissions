class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            query = target-nums[i]
            if query in lookup:
                return [lookup[query], i]
            
            lookup[nums[i]] = i
