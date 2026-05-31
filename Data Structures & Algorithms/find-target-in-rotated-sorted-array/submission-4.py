class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                # left is sorted
                if target < nums[l] or target > nums[m]:
                    # look on right side, past pivot point
                    l = m + 1
                else:
                    # look on left side
                    r = m - 1
            
            else: # nums[m] >= nums[m]
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m+1
        
        return -1
