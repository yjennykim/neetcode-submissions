class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] >= nums[l]:
                l = m
            else:
                r = m - 1
        
        # L biggest number
        if l == len(nums)-1:
            return nums[0]
        return nums[l+1]