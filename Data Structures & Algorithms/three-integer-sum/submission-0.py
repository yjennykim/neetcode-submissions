class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        if len(nums) < 3: return []

        for l in range(len(nums)-2):
            if l > 0 and nums[l] == nums[l - 1]:  # Skip duplicates for l
                continue
            m = l+1
            r = len(nums)-1

            while m < r:
                threesum = nums[m] + nums[l] + nums[r]
                if threesum < 0:
                    m += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                     
                    # Skip duplicates for m and r
                    while m < r and nums[m] == nums[m + 1]:
                        m += 1
                    # while m < r and nums[r] == nums[r - 1]:
                    #     r -= 1
                    
                    m += 1  # Move past the last valid m
                    r -= 1  # Move past the last valid r
            
        return res