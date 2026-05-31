class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search = {} # key, index

        for i, num in enumerate(nums):
            if target -  num in search:
                return [search[target - num], i]

            search[num] = i
        
        return -1
