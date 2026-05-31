import math
class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x *= -1
        
        val = int(''.join(list(reversed(str(x)))))
        if neg:
            val *= -1
        if val > math.pow(2,31)-1 or val < math.pow(-2, 31):
            return 0

        return val