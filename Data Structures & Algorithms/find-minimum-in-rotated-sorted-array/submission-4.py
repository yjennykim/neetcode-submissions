class Solution:
    def findMin(self, nums: List[int]) -> int:
       # minimum number in the array

       #  Input: nums = [3,4,5,6,1,2]
       # Output: 1
       # Smallest R 
        l,r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]: # sorted 
                r = m # keep in candidacy
            else:
                l = m + 1

        print('r', r) 
        return nums[r]

                