class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: Find the pivot index (the actual minimum element's location)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l  # This points directly to the minimum element
        
        # Step 2: Run a standard binary search on a VIRTUAL sorted array
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            m = (l + r) // 2
            
            # Shift mid by pivot, wrap around using % N
            real_mid = (m + pivot) % N
            
            if nums[real_mid] > target:
                r = m - 1
            elif nums[real_mid] < target:
                l = m + 1
            else:
                return real_mid 
                
        return -1