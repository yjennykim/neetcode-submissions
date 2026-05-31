class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return True if two strings contain same characters 
        if len(s) != len(t):
            return False
        
        counts = [0] * 26

        for letter in s:
            counts[ord(letter) - ord('a')] += 1
        
        for letter in t:
            i = ord(letter) - ord('a')
            counts[i] -= 1
            if counts[i] < 0: return False
        
        return True
        
        
        

