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
        l,r = 1, max(piles)
        rate = 0

        while l <= r:
            k = (l+r) // 2
            hrs = 0

            # simulation
            for pile in piles:
                hrs += math.ceil(pile / k)

            # took too long, eat more bananas
            if hrs > h:
                l = k + 1
            # eat less bananas
            else:
                r = k - 1
                rate = k

        return rate





