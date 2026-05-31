class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            
            # Compare mid with the rightmost element
            if nums[mid] > nums[right]:
                # Minimum must be in the right half
                left = mid + 1
            else:
                # Minimum is in the left half including mid
                right = mid
                
        # At the end of the loop, left == right, pointing to the minimum element
        return nums[left]