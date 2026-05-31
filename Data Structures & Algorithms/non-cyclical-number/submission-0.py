class Solution:
    def isHappy(self, n: int) -> bool:
        # set to check for infinite loop
        seen = set()

        # get sum of squares of digits
        while n != 1 and n not in seen:
            seen.add(n)

            val = 0
            while n > 0:
                print(f"Digit {n%10}")
                val += (n%10)**2
                n //= 10

            n = val
            print(f"Seen {n}") 
        
        if n == 1: 
            return True
            
        return False




                