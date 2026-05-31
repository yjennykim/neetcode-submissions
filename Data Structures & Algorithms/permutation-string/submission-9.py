class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count = {}
        for letter in s1:
            count[letter] = count.get(letter, 0) + 1

        matches = 0
        windowCount = {}
        for r in range(len(s2)):    
            # junk character (not a character in s1)
            if s2[r] not in count:
                l = r + 1
                matches = 0
                windowCount.clear()
                continue
            
            # too many
            while windowCount.get(s2[r], 0) >= count[s2[r]]:          
                if s2[l] in windowCount:
                    windowCount[s2[l]] -= 1
                    matches -= 1
                l += 1                

            windowCount[s2[r]] = windowCount.get(s2[r], 0) + 1
            matches += 1
            if matches == len(s1):
                return True
        
        return False
                        
            
            