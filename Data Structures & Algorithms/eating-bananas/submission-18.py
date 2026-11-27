class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        while l < r:
            m = (l + r) // 2
            
            time = 0
            for pile in piles:
                time += math.ceil(pile / m)
            
            # took too long, need to eat more
            if time > h: 
                l = m + 1
            else:
                # can eat less + take longer
                r = m
        
        return l