class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1_counts = {}
        for c in s1:
            if c not in s1_counts:
                s1_counts[c] = 0
            s1_counts[c] += 1

        l,r = 0,0
        s2_counts = {}
        while r < len(s2):
            # window size too big
            if r-l+1 > len(s1):
                print("window size too big", r-l+1)
                s2_counts[s2[l]] -= 1
                if s2_counts[s2[l]] == 0:
                    del s2_counts[s2[l]]
                l += 1
            
            if s2[r] not in s2_counts:
                s2_counts[s2[r]] = 0
            s2_counts[s2[r]] += 1

            r += 1
            
            # compare maps
            print('s2_counts', s2_counts)
            print('s1_counts', s1_counts)
            if s2_counts == s1_counts:
                return True
        
        return False


