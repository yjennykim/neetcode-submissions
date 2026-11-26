class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = set()
        l = 0
        for r in range(len(nums)):
            # clean up so window is size K
            if r-l > k:
                counter.remove(nums[l])
                l += 1

            if nums[r] in counter:
                return True

            counter.add(nums[r])
        
        return False
