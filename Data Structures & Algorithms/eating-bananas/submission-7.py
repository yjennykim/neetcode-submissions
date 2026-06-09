class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = rate of eating bananas
        # each hour, choose k bananas from pile. if pile < k, finish pile
        # minimum k to eat banans within h
        l,r = 1, max(piles) 

        # Biggest k possible
        while l < r:
            k = (l + r) // 2

            # Calculate if piles get eaten within h
            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(pile / k) 
            
            # Took too long. strict cut off
            if curr_hours > h:
                l = k + 1
            # keep as option, but try eating less bananas
            elif curr_hours <= h:
                r = k
            # else:
            #     return k
        
        return l
