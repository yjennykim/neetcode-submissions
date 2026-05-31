import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            [1, 2, 3, 4] , h = 9
            [4, 10, 23, 25]

            l = 1
            r = 4
            m = 2

            k = 6


            Try 2
            [1, 1, 2, 2] = 6 < 9 Good

            Try more bananas, 3
            []

        """
        piles.sort()
        l,r = 1, piles[-1]
        
        rate = 0
        while l <= r:
            m = (l+r) // 2
            hrs = 0

            # simulation
            for num in piles:
                hrs += math.ceil(num / m)
            print("When m=", m, "l=", l, "r=", r, "hrs=", hrs)

            # took too long, eat more bananas
            if hrs > h:
                l = m + 1
            # eat less bananas
            else:
                r = m - 1
                rate = m
                print("set rate", rate)

        return rate





