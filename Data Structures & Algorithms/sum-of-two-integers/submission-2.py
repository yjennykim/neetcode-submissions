class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0xFFFFFFFF  # To handle 32-bit integer overflow
        while b != 0:
            carry = a & b          # Calculate carry
            a = (a ^ b) & MAX      # Calculate sum without carry, mask to 32-bits
            b = carry << 1         # Shift carry to left for next iteration
        
        # Handle negative numbers and return the result
        return a if a <= 0x7FFFFFFF else ~(a ^ MAX)
