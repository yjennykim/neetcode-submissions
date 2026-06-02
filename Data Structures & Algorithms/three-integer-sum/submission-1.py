class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip repeat
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            l,r = i+1,len(nums)-1
            while l < r:
                if l == i: l += 1 
                if r == i: r -= 1

                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        
        return res
                

