class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # rate k
        # minimum k such that bananas within h hours
        # Smallest 
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            # took too long. eat more banansa
            if hours > h:
                l = k + 1
            else:
                # keep in candidacy. try eating less bananas
                r = k
        
        return r
            
