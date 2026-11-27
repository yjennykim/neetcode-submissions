class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            m = (l + r) // 2

            cap = m
            num_days = 1
            for weight in weights:  
                if cap - weight < 0:
                    num_days += 1
                    cap = m - weight
                else:
                    cap -= weight
            
            # took short time, can decrease weight capacity (valid candidate)
            if num_days <= days:
                r = m
            else:
                # took too long, need to increase weight capacity
                l = m + 1
        
        return l