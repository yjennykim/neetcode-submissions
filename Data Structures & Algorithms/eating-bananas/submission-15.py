class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum integer k to eat within h hours
        l = 1
        k = r = max(piles)

        while l < r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            # took too long, invalid
            if hours > h:
                l = k + 1
            # ate quickly, try eating less
            else:
                r = k

        return l


