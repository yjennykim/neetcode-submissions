class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            # if window too big now, shrink L
            if R-L > k:
                window.remove(nums[L])
                L += 1
            
            # Check if the NEW element (nums[R]) is already in our window
            if nums[R] in window:
                return True

            # R expands the window
            window.add(nums[R])
        
        return False