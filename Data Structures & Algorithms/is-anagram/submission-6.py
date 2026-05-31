from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return True if two strings contain same characters 
        if len(s) != len(t):
            return False
        
        counts = defaultdict(int)
        for letter in s:
            counts[letter] += 1
        
        for letter in t:
            if letter not in counts:
                return False
            
            counts[letter] -= 1
            if counts[letter] == 0:
                del counts[letter]
            
        # if empty, all letters were matched. Return true
        if counts:
            return False
        
        return True
        
        
        

