class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # search for min capacity
        l, r = max(weights), sum(weights)
        print(f"search space [{l},{r}]")

        while l < r:
            cap = (l + r) // 2
            d = 1
            s = cap
            for weight in weights:
                if s - weight >= 0:
                    # within cap
                    s -= weight
                else:
                    d += 1
                    s = cap - weight

            if d > days:
                # took too long, increase capacity
                l = cap + 1
            else:
                # potential candidate for min capacity
                r = cap
        
        return l
            
            