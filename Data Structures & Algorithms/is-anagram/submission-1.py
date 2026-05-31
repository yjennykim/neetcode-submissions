class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        frequency = {}
        for c in s:
            if c not in frequency:
                frequency[c] = 0
            frequency[c] += 1
        
        for c in t:
            if c not in frequency: 
                return False
            frequency[c] -= 1
            if c not in frequency:
                del frequency[c]
        
        return True if len(frequency) == 0 else False