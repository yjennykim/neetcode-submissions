class Solution:
    def mySqrt(self, x: int) -> int:
        # largest possible

        l,r = 0, x // 2 + 1
        while l < r:
            m = (l + r + 1) // 2
            res = m * m 
            if res < x:
                l = m
            elif res > x:
                r = m - 1
            else:
                print("Returning", m)
                return m
         
        return l 
            
