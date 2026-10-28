class Solution:
    def findMin(self, nums: List[int]) -> int:
        # look for first number that is ascending
        
        l, r = 0, len(nums)-1

        while l < r:
            m = (l + r) // 2
            
            # ascending, potential candidate
            if nums[m] <= nums[r]:
                r = m
            # descending, answer is somewhere in here
            else:
                l = m + 1

        return nums[l]