class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search = {} # key, index

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in search:
                return [search[compliment], i]

            search[num] = i
        
        return -1
