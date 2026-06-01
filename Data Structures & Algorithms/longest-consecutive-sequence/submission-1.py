from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bag = {} # number, seq cont
        longest = 0

        for num in nums:
            if num in bag:
                continue
            left = bag.get(num-1, 0)
            right = bag.get(num+1, 0)
  
            updated_freq = left + right + 1
            bag[num] = updated_freq
            
            # update boundaries
            if num-1 in bag:
                bag[num - left] = updated_freq 
            
            if num+1 in bag:
                bag[num + right] = updated_freq

            # get longest length
            longest = max(longest, updated_freq)
    
        return longest
